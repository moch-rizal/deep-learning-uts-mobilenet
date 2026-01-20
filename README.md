# Klasifikasi Gambar Kucing dan Anjing Menggunakan MobileNet

## Deskripsi

Proyek ini merupakan tugas UTS mata kuliah Deep Learning. Model menggunakan arsitektur MobileNetV2 berbasis transfer learning untuk melakukan klasifikasi dua kelas gambar, yaitu kucing dan anjing. Dataset menggunakan struktur folder `train` dan `test`, masing-masing berisi folder `kucing` dan `anjing`. Model dilatih menggunakan Google Colab dengan GPU T4 dan mencapai akurasi test sekitar 96%.

---

## Struktur Dataset
* dataset bisa di download melalui link berikut : https://www.kaggle.com/datasets/citranurjanah/kucing-dan-anjing-uas-ai
* Struktur folder dataset yang digunakan oleh notebook adalah sebagai berikut:

```
dataset/
├── train/
│   ├── kucing/
│   └── anjing/
└── test/
    ├── kucing/
    └── anjing/
```

---

## Cara Menjalankan

1.  Buka notebook `UTS_AnjingKucing_MobileNetV2.ipynb` di Google Colab.
2.  Aktifkan runtime GPU (`Runtime` > `Change runtime type` > `Hardware accelerator` > `GPU`).
3.  Jalankan semua cell secara berurutan.

---

## Hasil Model

* **Akurasi Test:** 96.15%
* **Jumlah kelas:** 2 (Cat & Dog)
* Precision, recall, dan F1-score di atas 0.95 pada kedua kelas.
* Confusion matrix menunjukkan prediksi benar pada hampir semua sampel.

---

## Identitas Mahasiswa

* **Nama:** Moch. Arif Samsul Rizal
* **NIM:** 202211420083
