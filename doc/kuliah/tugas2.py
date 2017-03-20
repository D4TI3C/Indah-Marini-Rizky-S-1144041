graph = {
             'Jl.Sarijadi': ['Jl.Sarirasa'],
             'Jl.Sarirasa': ['Jl.Terusan Prof DR.Sutami'],
             'Jl.Terusan Prof DR.Sutami': ['Jl.Surya Sumantri'],
             'Jl.Surya Sumantri': ['Jl.DR Djunjunan'],
             'Jl.DR Djunjunan': ['Jl.Layang Pasupati'],
             'Jl.Layang Pasupati': ['Jl.Pasir Kaliki'],
             'Jl.Pasir Kaliki': ['Jl.Sangkuning'],
             'Jl.Sangkuning': ['Istana Plaza'],        
        }

def rutepalingpendek(graph, lokasi_awal, lokasi_tujuan, rute=[]):
        rute = rute + [lokasi_awal]
        if lokasi_awal == lokasi_tujuan:
            return rute
            if not graph.has_key(lokasi_awal):
                    return None
        rutependek = None
        for node in graph[lokasi_awal]:
            if node not in rute:
                rutebaru = rutepalingpendek(graph, node, lokasi_tujuan, rute)
                if rutebaru:
                    if not rutependek or len(rutebaru) < len(rutependek):
                        rutependek = rutebaru
        return rutependek
print("Rute Jl.Sarijadi sampai Istana Plaza")
print("(Jl.Sarijadi-Jl.Sarirasa-Jl.Terusan Prof DR.Sutami-Jl.Surya Sumantri-Jl.DR Djunjunan-Jl.Layang Pasupati-Jl.Pasir Kaliki-Jl.Sangkuning-Istana Plaza")
print("Indah Marini Rizky Sihombing-11440041")
print("\n")
lokasi_awal = raw_input("Masukan Lokasi Awal : ")
lokasi_tujuan = raw_input("Masukan Lokasi Tujuan : ")
hasilnya = rutepalingpendek(graph, lokasi_awal, lokasi_tujuan, rute=[])
print "Rute Terpendek", hasilnya ,".",