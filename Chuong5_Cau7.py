def toi_uu_chuoi_danh_tu(chuoi):
   
    chuoi = chuoi.strip()
   
    tu = chuoi.split()
   
    tu = [t.capitalize() for t in tu]
    
    ket_qua = " ".join(tu)
    return ket_qua


# Ví dụ 
chuoi_vi_du = "   TRân    duY   thAnh   "
print(toi_uu_chuoi_danh_tu(chuoi_vi_du))
