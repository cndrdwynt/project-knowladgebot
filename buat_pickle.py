import pickle

data_statis_blsdm_super_lengkap = {
    "profil_dan_kontak": {
        "nama_lembaga": "BLSDM Komdigi Surabaya (Balai Pelatihan SDM Komunikasi dan Digital Surabaya)",
        "nama_lama": ["BPSDMP Kominfo Surabaya", "BPSDM Komdigi Surabaya"],
        "wilayah_kerja": "Jawa Timur dan Nusa Tenggara Barat (NTB)",
        "alamat": "Jl. Raya Ketajen No. 36, Gedangan, Kabupaten Sidoarjo, Jawa Timur 61254",
        "telepon_kantor": "(031) 8011944",
        "whatsapp_admin": "082331841722",
        "website": "https://bpsdm.komdigi.go.id/upt/surabaya",
        "instagram": "@blsdm.komdigi.surabaya",
        "jam_operasional_publik": "Senin s.d. Jumat pukul 08.00 hingga 16.00 WIB",
        "nama_kepala": "Bagus Winarko",
        "jenis_upt": "Balai Pelatihan"
    },
    "aturan_akun": {
        "aturan_nik": "1 NIK hanya bisa digunakan untuk 1 akun Digital Talent",
        "syarat_password": "Minimal 8 karakter, kombinasi huruf besar, kecil, angka, dan karakter spesial (@$!%?&)",
        "pilihan_status_pekerjaan": ["Pelajar/Mahasiswa", "Bekerja", "Tidak Bekerja"],
        "batas_ubah_domisili": "Maksimal 2 kali dalam satu bulan"
    },
    "struktur_program_dta": {
        "kepanjangan_dta": "Digital Talent Academy",
        "tiga_program_utama": ["KDD (Keterampilan Digital Dasar)", "GTA (Government Transformation Academy)", "Talenta Digital"],
        "subprogram_talenta_digital": ["AITF", "VBL", "DEX"],
        "subprogram_dex": ["F-DEX (Future Talent Track)", "P-DEX (Professional Track)"],
        "target_peserta": {
            "KDD": "UMKM, koperasi, masyarakat umum, kelompok tematik, pekerja kreatif, komunitas pekerja lepas",
            "GTA": "ASN K/L/D, TNI, dan Polri",
            "AITF": "Lembaga pendidikan tinggi (universitas)",
            "VBL": "Mahasiswa vokasi dan siswa SMK",
            "F-DEX": "Siswa SMA, mahasiswa (Diploma, Sarjana, Magister)",
            "P-DEX": "Masyarakat umum, pelaku dunia usaha, industri, dan dunia kerja"
        }
    },
    "info_rekrutmen_kerja": {
        "jalur_resmi": "Seleksi CPNS nasional via https://sscasn.bkn.go.id",
        "status_rekrutmen_mandiri": "BLSDM Komdigi Surabaya tidak membuka rekrutmen tenaga kontrak atau PPNPN secara mandiri"
    },
    "info_magang": {
        "status_pemagang": "Praktikan (bukan pegawai atau kontrak)",
        "sasaran": "Mahasiswa aktif D3, D4, atau S1",
        "durasi_magang": "Minimal 3 bulan, maksimal 6 bulan",
        "jadwal_praktik_senin_kamis": "08.00–16.00 WIB",
        "jadwal_praktik_jumat": "08.30–16.30 WIB",
        "waktu_istirahat": "12.00–13.00 WIB",
        "platform_pendaftaran": "Website SIMANOV",
        "kewajiban": ["Logbook harian", "Seragam (Putih-Hitam/Almamater)", "Laporan Akhir", "Project Akhir"]
    },
    "info_pelatihan_dan_sertifikat": {
        "jalur_pendaftaran": ["Microskill", "Digital Talent Academy (DTA)"],
        "ketersediaan_microskill": "Selalu terbuka dan bisa diakses kapan saja",
        "waktu_turun_sertifikat_microskill": "Maksimal 4 minggu hari kerja",
        "waktu_turun_sertifikat_dta": "Maksimal 2 minggu di luar masa pendampingan",
        "status_sertifikasi_gta": "Tidak ada proses sertifikasi, hanya sertifikat kelulusan"
    },
    "tema_pelatihan_gta": {
        "kebijakan_2026": [
            "Analisa Kota Cerdas", "Pemanfaatan AI untuk Pemerintahan", "AI for Content Creation", 
            "Junior Network Administration", "Video Production for Government Campaign", 
            "Fasilitator Pembelajaran Digital Dasar", "Fasilitator Pembelajaran Digital Menengah", 
            "Junior Office Operator", "Generative AI untuk Peningkatan Kerja ASN"
        ],
        "kebijakan_2023": [
            "IT Essentials", "Business Process Engineer", "IT Business Analyst", "Digital Public Relations", 
            "Social Media Analyst", "Analis Kota Cerdas", "Fasilitator Pembelajaran Digital", 
            "Data Science Fundamental", "Junior Network Administrator", "Junior Graphic Design", 
            "Junior Office Operator", "Manajemen Proyek", "Cybersecurity Essentials", "Manajemen Risiko SPBE", 
            "Sistem Manajemen Keamanan Informasi ISO 27001", "Audit Internal ISO 19011", 
            "Sistem Manajemen Layanan TI ISO 20000", "Arsitektur SPBE", "Video Production", 
            "TIK Dasar", "Python Essentials 1"
        ]
    },
    "standar_kelulusan_gta_umum": {
        "batas_absen_maksimal": "10% dari total Jam Pelatihan",
        "nilai_minimal_lulus": 65,
        "bobot_penilaian": "Pre-Test 5%, Tugas 65%, Post-Test 30%"
    },
    "silabus_gta_detail": {
        "ADEFR": {
            "kepanjangan": "Associate Digital Evidence First Responder",
            "durasi": "24 JP",
            "jadwal_periode": "Februari – Oktober 2025",
            "syarat_pendidikan": "Minimal D3 Teknik Informatika / Sistem Informasi / Ilmu Komputer",
            "spek_laptop": "RAM 8 GB, Media penyimpanan minimal 256 GB"
        },
        "AI_for_Content_Creation": {
            "kepanjangan": "Artificial Intelligence for Content Creation",
            "durasi": "22 JP",
            "jadwal_periode": "Februari – Desember 2025",
            "syarat_pendidikan": "Minimal SMA",
            "spek_laptop": "RAM minimal 4 GB, Ruang penyimpanan kosong minimal 1,5 GB"
        },
        "AIP": {
            "kepanjangan": "AI Praktis untuk Produktivitas",
            "durasi": "22 JP (Wajib) + 40 JP (Bonus) + 8 JP (Luring)",
            "jadwal_periode": "Oktober – Desember 2025",
            "syarat_khusus": "KHUSUS ASN Kementerian Komdigi, usia maksimal 55 tahun",
            "spek_laptop": "RAM minimal 2 GB"
        },
        "Analis_Kota_Cerdas": {
            "kepanjangan": "Analis Kota Cerdas SNI ISO 37122:2019",
            "durasi": "22 JP",
            "jadwal_periode": "Mei – Desember 2025",
            "syarat_khusus": "KHUSUS ASN pemerintah kota/kabupaten",
            "spek_laptop": "RAM minimal 2 GB, terinstall Zoom/Webex"
        },
        "Arsitektur_Keamanan_SPBE": {
            "kepanjangan": "Arsitektur Keamanan SPBE",
            "durasi": "30 JP",
            "jadwal_periode": "Februari – Desember 2025",
            "syarat_pendidikan": "Minimal D3 Sistem Informasi / Teknik Informatika / Keamanan Informasi",
            "spek_laptop": "RAM minimal 2 GB"
        },
        "Arsitektur_SPBE": {
            "kepanjangan": "Arsitektur SPBE",
            "durasi": "42 JP",
            "jadwal_periode": "Februari – Desember 2025",
            "syarat_khusus": "Masa kerja minimal 2 tahun, HANYA tersedia Full Offline",
            "spek_laptop": "RAM minimal 2 GB"
        },
        "Audit_Keamanan_SPBE": {
            "kepanjangan": "Audit Keamanan SPBE",
            "durasi": "36 JP",
            "jadwal_periode": "Februari – Oktober 2025",
            "syarat_pendidikan": "Minimal S1",
            "spek_laptop": "RAM minimal 4 GB"
        },
        "BPE": {
            "kepanjangan": "Business Process Engineer",
            "durasi": "60 JP",
            "jadwal_periode": "Februari – Desember 2025",
            "syarat_khusus": "Pengalaman kerja minimal 6 bulan",
            "spek_laptop": "RAM minimal 4 GB, Wajib terinstall Visual Paradigm"
        },
        "Data_Science_Fundamental": {
            "kepanjangan": "Data Science Fundamental",
            "durasi": "40 JP",
            "jadwal_periode": "Februari – Desember 2025",
            "syarat_pendidikan": "Minimal D3",
            "spek_laptop": "RAM minimal 4 GB, Storage 1.5 GB, Wajib terinstall RapidMiner"
        },
        "Edukasi_Kesadaran_Keamanan_SPBE": {
            "kepanjangan": "Edukasi Kesadaran Keamanan SPBE",
            "mitra": "BSSN",
            "durasi": "12 JP",
            "metode": ["Self-Paced Learning (SPL)"],
            "jadwal_periode": "Februari – Desember 2025",
            "syarat_pendidikan": "Semua jenjang (ASN/TNI/Polri/Non-ASN)",
            "syarat_khusus": "Maksimal 53 tahun",
            "spek_laptop": "RAM minimal 2 GB",
            "standar_kelulusan_khusus": "Menyelesaikan seluruh materi, kuis (nilai minimal 70), dan post-test"
        },
        "FPD": {
            "kepanjangan": "Fasilitator Pembelajaran Digital",
            "durasi": "36 JP",
            "jadwal_periode": "Februari – Desember 2025",
            "syarat_pendidikan": "Minimal D3",
            "syarat_khusus": "Diutamakan Widyaiswara/Pengajar/Dosen/Fasilitator, maksimal 53 tahun",
            "spek_laptop": "RAM minimal 4 GB"
        },
        "FPDM": {
            "kepanjangan": "Fasilitator Pembelajaran Digital Menengah",
            "durasi": "38 JP",
            "jadwal_periode": "Februari – Desember 2025",
            "syarat_pendidikan": "Minimal D3",
            "syarat_khusus": "WAJIB telah lulus pelatihan Fasilitator Pembelajaran Digital (FPD) sebelumnya",
            "spek_laptop": "RAM minimal 4 GB"
        },
        "Generative_AI_Kinerja_ASN": {
            "kepanjangan": "Generative AI untuk Peningkatan Kinerja ASN",
            "mitra": "Microsoft",
            "durasi": "18 JP",
            "jadwal_periode": "Mei – Desember 2025",
            "syarat_pendidikan": "Minimal D3",
            "spek_laptop": "RAM minimal 4 GB"
        },
        "ITBA": {
            "kepanjangan": "Information Technology Business Analyst",
            "durasi": "50 JP",
            "jadwal_periode": "Februari – Desember 2025",
            "syarat_pendidikan": "Minimal D3 Sistem Informasi/Ilmu Komputer/Teknik Informatika ATAU memiliki pengalaman IT",
            "spek_laptop": "RAM minimal 4 GB, Wajib terinstall Visual Paradigm dan Draw.io"
        },
        "JGD": {
            "kepanjangan": "Junior Graphic Designer",
            "durasi": "40 JP",
            "jadwal_periode": "Februari – Desember 2025",
            "syarat_pendidikan": "Minimal SMA/SMK sederajat",
            "spek_laptop": "RAM minimal 4 GB (disarankan 8 GB), Wajib terinstall Adobe Photoshop/Illustrator/CorelDraw/Canva"
        },
        "JNA": {
            "kepanjangan": "Junior Network Administrator",
            "mitra": "Berbagai K/L",
            "durasi": "45 JP",
            "jadwal_periode": "Februari – Desember 2025",
            "syarat_pendidikan": "Minimal SMA/SMK sederajat",
            "spek_laptop": "RAM minimal 4 GB, Wajib terinstall aplikasi Cisco Packet Tracer"
        },
        "JOO": {
            "kepanjangan": "Junior Office Operator",
            "durasi": "40 JP",
            "jadwal_periode": "Februari – Desember 2025",
            "syarat_pendidikan": "Minimal D3",
            "spek_laptop": "RAM minimal 4 GB, Wajib terinstall Microsoft Office"
        },
        "Manajemen_Proyek": {
            "kepanjangan": "Manajemen Proyek",
            "durasi": "40 JP",
            "jadwal_periode": "Februari – Desember 2025",
            "syarat_pendidikan": "Minimal D3",
            "spek_laptop": "RAM minimal 2 GB"
        },
        "Manajemen_Risiko_Keamanan_SPBE": {
            "kepanjangan": "Manajemen Risiko Keamanan SPBE",
            "mitra": "BSSN",
            "durasi": "36 JP",
            "jadwal_periode": "Februari – Oktober 2025",
            "syarat_pendidikan": "Minimal S1 Ilmu Komputer/Teknik Informatika/Sistem Informasi ATAU pengalaman di bidang terkait",
            "spek_laptop": "RAM minimal 2 GB"
        },
        "Manajemen_Risiko_SPBE": {
            "kepanjangan": "Manajemen Risiko SPBE",
            "durasi": "35 JP",
            "jadwal_periode": "Februari – Desember 2025",
            "syarat_pendidikan": "Minimal D3",
            "syarat_khusus": "Wajib membawa Dokumen Renstra, Perjanjian Kinerja, dan Rencana Kerja Instansi",
            "spek_laptop": "Standard (RAM minimal 2GB - 4GB)"
        },
        "Next_Gen_ASN": {
            "kepanjangan": "Next-Gen ASN: Leading with AI",
            "durasi": "7 JP (1 Hari Pelaksanaan)",
            "jadwal_periode": "Batch 1 (30 Sep 2025) & Batch 2 (1 Okt 2025)",
            "syarat_pendidikan": "Semua jenjang",
            "syarat_khusus": "KHUSUS ASN, batas usia MAKSIMAL 35 TAHUN, Hanya tersedia metode Full Offline",
            "spek_laptop": "RAM minimal 4 GB (disarankan 8 GB)"
        },
        "Pemanfaatan_AI_Pemerintahan": {
            "kepanjangan": "Pemanfaatan AI di Pemerintahan",
            "durasi": "32 JP",
            "jadwal_periode": "Februari – Desember 2025",
            "syarat_pendidikan": "Minimal D3",
            "syarat_khusus": "Maksimal 53 tahun, tidak sedang menempuh pendidikan formal",
            "spek_laptop": "RAM minimal 4 GB"
        },
        "Penanganan_Insiden_Keamanan_SPBE": {
            "kepanjangan": "Penanganan Insiden Keamanan SPBE",
            "mitra": "BSSN",
            "durasi": "40 JP",
            "jadwal_periode": "Maret – Desember 2025",
            "syarat_pendidikan": "Minimal S1",
            "syarat_khusus": "Diutamakan pegawai pengelola SI/TI/Keamanan Informasi",
            "spek_laptop": "RAM MINIMAL 8 GB, Wajib terinstall virtualisasi Ubuntu Server 22.04 LTS dan Kali Linux (VMware/VirtualBox)"
        },
        "Penilaian_Kerentanan_Keamanan_SPBE": {
            "kepanjangan": "Penilaian Kerentanan Keamanan SPBE",
            "mitra": "BSSN",
            "durasi": "39 JP",
            "jadwal_periode": "Februari – Desember 2025",
            "syarat_pendidikan": "Minimal D3",
            "syarat_khusus": "KHUSUS ASN (Non-ASN/TNI/Polri tidak diperkenankan)",
            "spek_laptop": "RAM minimal 8 GB, laptop wajib memiliki fungsi virtualisasi aktif"
        },
        "Penyusunan_Kebijakan_Keamanan_SPBE": {
            "kepanjangan": "Penyusunan Kebijakan Keamanan SPBE",
            "mitra": "BSSN",
            "durasi": "35 JP",
            "jadwal_periode": "Februari – Desember 2025",
            "syarat_pendidikan": "Minimal S1",
            "syarat_khusus": "KHUSUS PNS/TNI/Polri (Non-ASN dilarang), MINIMAL Pangkat Golongan III/a",
            "spek_laptop": "RAM minimal 4 GB"
        },
        "SMKI": {
            "kepanjangan": "Sistem Manajemen Keamanan Informasi SNI ISO/IEC 27001:2022",
            "durasi": "50 JP",
            "jadwal_periode": "Februari – Desember 2025",
            "syarat_pendidikan": "Minimal D3 (diutamakan rumpun Komputer/IT)",
            "syarat_khusus": "Khusus ASN K/L/D, Pengalaman di bidang IT minimal 1 tahun",
            "spek_laptop": "RAM minimal 2 GB"
        },
        "SMLTI": {
            "kepanjangan": "Sistem Manajemen Layanan Teknologi Informasi (SNI ISO/IEC 20000-1:2018)",
            "mitra": "BSN",
            "durasi": "40 JP",
            "jadwal_periode": "Februari – Desember 2025",
            "syarat_pendidikan": "Minimal D3",
            "syarat_khusus": "Maksimal usia 50 Tahun, Wajib mengerti Bahasa Inggris Dasar",
            "spek_laptop": "Standard (RAM minimal 2GB - 4GB)"
        },
        "Social_Media_Analyst": {
            "kepanjangan": "Social Media Analyst",
            "durasi": "26 JP",
            "jadwal_periode": "Februari – Desember 2025",
            "syarat_pendidikan": "Minimal D3",
            "syarat_khusus": "Batas usia MAKSIMAL 45 TAHUN, tidak sedang menempuh pendidikan formal",
            "spek_laptop": "RAM minimal 4 GB"
        },
        "TIK_MI": {
            "kepanjangan": "Dasar Teknologi Informasi dan Komunikasi untuk Media Informasi",
            "durasi": "40 JP",
            "jadwal_periode": "Februari – Oktober 2025",
            "syarat_pendidikan": "Tidak dibatasi secara spesifik",
            "syarat_khusus": "Diutamakan unsur bagian Publikasi dan Dokumentasi",
            "spek_laptop": "RAM minimal 8 GB"
        },
        "Video_Production": {
            "kepanjangan": "Video Production for Government Campaign",
            "mitra": "BPPTIK Cikarang",
            "durasi": "40 JP",
            "jadwal_periode": "Februari – Desember 2025",
            "syarat_pendidikan": "Minimal D3",
            "syarat_khusus": "Diutamakan pejabat fungsional Pranata Humas, Tenaga Pengajar/Pendidik, dan Pengelola Informasi/Kehumasan",
            "spek_laptop": "RAM MINIMAL 8 GB"
        },
        "Visualisasi_Data": {
            "kepanjangan": "Visualisasi Data",
            "durasi": "30 JP",
            "jadwal_periode": "Februari – Desember 2025",
            "syarat_pendidikan": "Minimal D3",
            "syarat_khusus": "Peserta wajib menguasai operasi dasar aplikasi Microsoft Excel",
            "spek_laptop": "RAM minimal 4 GB (disarankan 8 GB)"
        }
    }
}

# Menyimpan ulang ke file Pickle
with open('data_statis_blsdm_final.pkl', 'wb') as file:
    pickle.dump(data_statis_blsdm_super_lengkap, file)

print("Update Final Selesai! Seluruh data mutlak dari seluruh file GTA sudah diamankan.")