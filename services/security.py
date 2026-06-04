import ipaddress

BLOCKED_RANGES = [
    ipaddress.ip_network("169.254.0.0/16"),   # 클라우드 메타데이터 (AWS/GCP/Oracle)
    ipaddress.ip_network("100.64.0.0/10"),    # CGNAT
    ipaddress.ip_network("0.0.0.0/8"),        # 자기 자신
    ipaddress.ip_network("224.0.0.0/4"),      # 멀티캐스트
]

def validate_target_ip(ip_str: str) -> tuple[bool, str]:
    """
    입력된 IP가 외부 접근에 안전한지 검증합니다.
    (로컬 진단 모드이므로 사설 IP나 localhost는 허용하되, 오라클 서버 자체의 메타데이터 등 민감한 IP만 차단합니다)
    """
    try:
        if ip_str.lower() == "localhost":
            addr = ipaddress.ip_address("127.0.0.1")
        else:
            addr = ipaddress.ip_address(ip_str)
            
        for blocked in BLOCKED_RANGES:
            if addr in blocked:
                return False, f"보안 상의 이유로 차단된 IP 대역({blocked})입니다."
                
        return True, ""
    except ValueError:
        return False, "올바른 형식의 IP 주소가 아닙니다."
