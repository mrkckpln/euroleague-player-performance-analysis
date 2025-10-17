# 🏀 Euroleague Oyuncu Performans Analizi

Bu proje, Kaggle'dan alınan kapsamlı Euroleague basketbol veri setini kullanarak oyuncu performansını ve değerlemesini etkileyen temel faktörleri ortaya çıkarmak için derinlemesine bir istatistiksel analiz sunar. Proje, OSTİM Teknik Üniversitesi MATH 204 dersi kapsamında hazırlanmıştır.

## 💡 Ana Bulgular ve İçgörüler

1) Oyuncu Pozisyonu, Değerlemede Baskın Bir Faktördür
- ANOVA testi, oyuncu verimlilik puanlarının (`valuation_per_game`) pozisyonlar arasında istatistiksel olarak anlamlı farklılıklar gösterdiğini doğrulamıştır ($p < 0.05$).
- Pozisyon, oyuncu değerlemesindeki varyansın yaklaşık %45.8'ini açıklar ($\eta^{2} = 0.458$).
- Değerleme hiyerarşisi: Pivot (Center, ort. 14.02) > Forvet (Forward, ort. 13.33) > Gard (Guard, ort. 11.53).

2) Oyuncu Performansı Yüksek Doğrulukla Tahmin Edilebilir
- Sayı, ribaund ve asist metriklerini kullanan çoklu doğrusal regresyon modeli, maç başına değerlemeyi yüksek doğrulukla açıklar ($R^{2} = 0.925$).
- Bu üç istatistik arasında değerlemeyi tahmin etmede en etkili olan değişken maç başına sayıdır (`points_per_game`).

3) Temel İstatistikler Güçlü Pozitif Korelasyonlar Gösterir
- Korelasyon matrisi; sayı, ribaund, asist ve top çalma gibi metriklerin birbiriyle pozitif ilişkili olduğunu göstermektedir.
- Örneğin, maç başına sayı ile toplam ribaund arasında güçlü bir ilişki (≈ 0.66) bulunmaktadır.

4) Daha Fazla Süre, Daha Yüksek Verimlilik Anlamına Gelir
- Oynanan dakika ile verimlilik puanı arasında orta düzeyde pozitif bir korelasyon (≈ 0.62) vardır.
- Bu, daha fazla sorumluluk alan oyuncuların genellikle daha verimli olma eğiliminde olduğunu destekler.

Not: Yukarıdaki sonuçlar bu projede kullanılan veri örneği ve model varsayımlarına göredir; farklı sezonlar veya alt-kümelerde değerler değişebilir.

## 📈 Analiz Adımları

- Veri Temizleme ve Ön İşleme: Ham verilerin birleştirilmesi, aykırı değer/eksik veri yönetimi, türetilmiş metrikler.
- Tanımlayıcı İstatistikler: Ortalama, standart sapma, dağılım özetleri ve temel görselleştirmeler.
- Dağılım Analizi: Sayı, ribaund ve asist gibi metriklerin dağılımlarının incelenmesi.
- Korelasyon Analizi: Temel istatistikler arasındaki ilişkilerin gücü ve yönü.
- ANOVA Testi: Pozisyonlara göre verimlilik farklarının test edilmesi.
- Doğrusal Regresyon: `points_per_game`, `rebounds_per_game`, `assists_per_game` ile `valuation_per_game` tahmin modeli.

## 🖼️ Görseller (Öne Çıkanlar)

- Verilerin tanımlayıcı özetini gösteren grafik:

	![Tanımlayıcı İstatistikler - Histogramlar ve boxplotlar; eksenler: metrik değerleri, oyuncu sayısı. Üretildi: `distribution_analysis.py`.](images/descriptive_statistics_euroleague.png)
	**Açıklama:** Bu görsel, temel metriklerin (points, rebounds, assists vb.) dağılımlarını histogram ve boxplot kombinasyonuyla gösterir. X ekseni metrik değerlerini; Y ekseni frekansı/oyuncu sayısını gösterir. Aykırı değerler ve dağılımın çarpıklığı hakkında hızlı bilgi verir.

- Korelasyon matrisi (ısı haritası) — temel metriklerin ilişkileri:

	![Korelasyon Matrisi - Isı haritası; eksenler: metrik isimleri; renk: Pearson korelasyon katsayısı. Üretildi: `correlation_calculation.py`.](images/correlation_matrix.png)
	**Açıklama:** Metin hücreleri ve renk kodlaması metrik çiftleri arasındaki Pearson korelasyonlarını gösterir. Öne çıkan ilişki: points ile rebounds ~0.66; minutes ile valuation arasında ~0.62 gibi pozitif korelasyonlar gözlemleniyor.

- Pozisyona göre verimlilik karşılaştırması (violin/box):

	![Pozisyona Göre Verimlilik - Violin/boxplot; eksenler: pozisyon (x), valuation_per_game (y). Üretildi: `efficiency_points_analysis.py` / `efficiency_violin_plot_position`.](images/efficiency_violin_plot_position.png)
	**Açıklama:** Pozisyonlara göre verimlilik dağılımlarını gösterir. Merkezi eğilim ve dağılım genişliği gözlemlenebilir. ANOVA sonuçlarıyla tutarlı olarak Centers (Pivot) ortalamaları ve dağılımın üst sınırları diğer pozisyonlardan yüksektir.

- Oynama süresi ile verimlilik ilişkisi:

	![Oynama Süresi ve Verimlilik - Scatter + trendline; eksenler: minutes_per_game (x), valuation_per_game (y). Üretildi: `playing_time_analysis.py`.](images/playing_time_efficiency_analysis.png)
	**Açıklama:** Scatter plot üzerinde çizilen trendline, oynanan dakika arttıkça verimlilikte (valuation) pozitif bir eğilim olduğunu gösterir (r ≈ 0.62). Bu grafik özellikle düşük dakika aralığında değişkenliği vurgular.

- Regresyon: Gerçek vs Tahmin edilen değerlemeler:

	![Regresyon - Gerçek vs Tahmin (scatter); eksenler: gerçek valuation (x), tahmin edilen valuation (y). Üretildi: `euroleague_analysis.py` / regresyon modülü.](images/regression_actual_vs_predicted.png)
	**Açıklama:** Modelin performansını görselleştirir; idealde noktalar y = x doğrusu üzerinde toplanır. Bu model için $R^{2} \approx 0.925$ gibi yüksek bir açıklama gücü raporlanmıştır; points_per_game en kuvvetli katkıyı sağlar.

- Öne çıkan oyuncular / üst 10 oyuncu (örnek):

	![Öne Çıkan Oyuncular - Bar chart/top10; eksenler: oyuncu isimleri (y), ortalama valuation_per_game (x). Üretildi: `efficiency_points_analysis.py`.](images/outstanding_players_top10_euroleague.png)
	**Açıklama:** Ortalama verimliliklerine göre üst 10 oyuncuyu listeler. Bu görsel, bireysel oyuncu performansını takım/pozisyon bağlamında karşılaştırmak için kullanışlıdır.

## 🧰 Proje Yapısı

- `euroleague_analysis.py`: Ana çalışma akışı, verilerin yüklenmesi ve özet analizlerin tetiklenmesi.
- `anova_analysis.py`: Pozisyona göre ANOVA ve etki büyüklüğü (örn. $\eta^2$) hesapları.
- `correlation_calculation.py`: Korelasyon matrisi/ısı haritası ve seçili metrik ilişkileri.
- `distribution_analysis.py`: Temel metriklerin dağılım incelemeleri ve görselleri.
- `efficiency_points_analysis.py`: Verimlilik puanı ile sayı/diğer metriklerin ilişkileri.
- `playing_time_analysis.py`: Oynama süresi ile verimlilik arasındaki ilişkinin incelenmesi.
- `requirements.txt`: Gerekli Python paketleri.
- `Euroleague_data/`: Çalışmada kullanılan CSV veri dosyaları.

## ⚙️ Kurulum ve Çalıştırma

Öneri: Adımları projenin kök dizininde (bu dosyanın bulunduğu klasör) çalıştırın.

1) Sanal ortam oluşturun (önerilir)
```powershell
python -m venv venv
```

2) Sanal ortamı aktif edin (Windows PowerShell)
```powershell
./venv/Scripts/Activate.ps1
```

3) Gerekli paketleri yükleyin
```powershell
pip install -r requirements.txt
```

4) Analizi çalıştırın (tüm akış)
```powershell
python .\euroleague_analysis.py
```

İsteğe bağlı olarak alt analiz betiklerini ayrı ayrı da çalıştırabilirsiniz:
```powershell
python .\anova_analysis.py
python .\correlation_calculation.py
python .\distribution_analysis.py
python .\efficiency_points_analysis.py
python .\playing_time_analysis.py
```

## 📊 Veri Seti

Bu analizde, Euroleague'in en üst düzey profesyonel basketbol müsabakalarına ait takım ve oyuncu istatistiklerini içeren bir Kaggle veri seti kullanılmıştır.

-– Veri kaynağı: Kaggle – Euroleague Datasets: https://www.kaggle.com/datasets/babissamothrakis/euroleague-datasets

Kullanım notu:
- İlgili veri setini Kaggle üzerinden indirdikten sonra CSV dosyalarını `Euroleague_data/` klasörü altına yerleştiriniz.
- Veri erişim kuralları ve lisans koşulları için Kaggle sayfasını kontrol ediniz.