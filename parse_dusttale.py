import struct, os, sys, hashlib

def parse_game(filepath):
    data = open(filepath, 'rb').read()
    total = len(data)
    print(f"📦 {os.path.basename(filepath)}")
    print(f"   Size: {total:,} bytes ({total/1024/1024:.1f} MB)")

    # === 根 FORM / GEN8 头 ===
    # 开头是 4字节填充 + 4字节 "BxT" + 4字节版本号("GEN8") + 4字节 chunk 数(或偏移)
    # 实际上 GM8 结构: header 固定 528 字节, 后面是各个 chunk
    # 更稳妥: 直接扫描有效 chunk (name + size 满足范围)

    valid_chunks = []
    pos = 0
    seen = set()
    
    # 先跳过高版本 header 区域 (大概 528 - 800 字节)
    # 但我们要找: 在每个已知 chunk 名后, 其 size 必须满足
    #   1) size > 16
    #   2) pos + 8 + size <= total (不越界)
    #   3) size 本身不是另一个有效的 chunk header
    
    known_names = {
        b'GEN8', b'SOND', b'SPRT', b'BGND', b'AGRP', b'SCPT',
        b'CODE', b'FONT', b'DXBC', b'ROOM', b'OBJ ', b'VAR ',
        b'STRG', b'TOBJ', b'TGME', b'TTRG', b'TFNT', b'TAUD',
        b'TSND', b'TSPR', b'TBGD', b'TLNG', b'PTH ', b'GLOB',
        b'SHDR', b'TMXL', b'TPNT', b'TGRP', b'TDS ', b'FUNC',
    }

    # 分 3 步走:
    # Step 1: 从头部拿 chunk 表
    # 但 GM 8.1 的结构可能不同, 先尝试暴力扫描 + 交叉验证
    
    for pos in range(0, total - 8):
        name = data[pos:pos+4]
        if name not in known_names:
            continue
        size = struct.unpack('<I', data[pos+4:pos+8])[0]
        end = pos + 8 + size
        if not (8 < size < total * 0.8):
            continue
        if end > total:
            continue
        if (name, pos) in seen:
            continue
        seen.add((name, pos))
        valid_chunks.append((pos, size, name.decode()))
    
    valid_chunks.sort()
    
    print(f"\n📋 识别到 {len(valid_chunks)} 个有效 chunk:")
    print(f"   {'NAME':5s} {'OFFSET':>12s} {'SIZE':>14s}")
    print(f"   {'-'*5} {'-'*12} {'-'*14}")
    
    for pos, size, name in valid_chunks:
        print(f"   {name:5s} {pos:>12,} {size:>14,}  ({size/1024:.1f} KB)")
    
    return data, valid_chunks

def extract_chunk(data, pos, size, name, outdir):
    path = os.path.join(outdir, f"{name}_{pos:x}.bin")
    os.makedirs(outdir, exist_ok=True)
    with open(path, 'wb') as f:
        f.write(data[pos+8:pos+8+size])
    return path

def extract_strings(data, outdir):
    """提取所有可见字符串, 用于找对话/标题/物品名"""
    strings = set()
    cur = b''
    for b in data:
        if 0x20 <= b <= 0x7e or b in (0x0a, 0x0d):
            cur += bytes([b])
        else:
            if len(cur) >= 4:
                strings.add(cur.decode('ascii', errors='replace'))
            cur = b''
    if len(cur) >= 4:
        strings.add(cur.decode('ascii', errors='replace'))
    
    os.makedirs(outdir, exist_ok=True)
    with open(os.path.join(outdir, 'all_strings.txt'), 'w', encoding='utf-8') as f:
        for s in sorted(strings):
            f.write(s + '\n')
    
    return len(strings)

def detect_formats(data, chunks, outdir):
    """识别每个 chunk 的内部格式, 尝试导出"""
    results = []
    
    for pos, size, name in chunks:
        chunk_data = data[pos+8:pos+8+size]
        head_hex = chunk_data[:8].hex()
        
        info = f"{name}@{pos:x} size={size:,}"
        extra = ""
        
        if name == 'SOND':
            # 音频表: 可能有 WAV/OGG 内嵌
            # 找 RIFF (WAV) 或 OggS (OGG) 或 KONTAKT
            wav_count = chunk_data.count(b'RIFF')
            ogg_count = chunk_data.count(b'OggS')
            extra = f"WAV={wav_count} OGG={ogg_count}"
        elif name == 'FONT':
            png_count = chunk_data.count(b'\x89PNG')
            extra = f"PNG spritesheets={png_count}"
        elif name == 'ROOM':
            # 可能是 tile map 定义
            extra = f"tilemap chunk, head={head_hex}"
        elif name == 'CODE':
            # GameMaker 代码 (编译后的, 有字符串表)
            extra = f"code section (compiled GML), strings embedded"
        elif name == 'SPRT':
            png_count = chunk_data.count(b'\x89PNG')
            extra = f"sprites, PNG blobs={png_count}"
        
        results.append((name, pos, size, extra or head_hex[:16]))
    
    return results

# === 主流程 ===
filepath = 'apk_extracted/assets/game.droid'
data, chunks = parse_game(filepath)

outdir = 'dusttale_extracted'
os.makedirs(outdir, exist_ok=True)

print(f"\n💾 导出 chunks -> {outdir}/")
for pos, size, name in chunks:
    p = extract_chunk(data, pos, size, name, os.path.join(outdir, 'chunks'))
    print(f"  ✅ {os.path.basename(p)}")

results = detect_formats(data, chunks, outdir)

print(f"\n🔍 格式详情:")
for name, pos, size, info in results:
    print(f"  {name:5s} ({size/1024:>8.1f} KB)  {info}")

n = extract_strings(data, outdir)
print(f"\n📝 提取了 {n:,} 个可见字符串 -> {outdir}/all_strings.txt")

print(f"\n✨ 完成!")
