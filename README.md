# 🛡️ Multi-SIEM Aşkarlama və Avtomatlaşdırma Çərçivəsi (Splunk & QRadar)

## 📌 Layihə Haqqında Ümumi Məlumat
Bu layihə, **Splunk Enterprise** və **IBM QRadar SIEM** platformalarını vahid bir ekosistemdə birləşdirərək, müasir **"Detection as Code" (DaC)** yanaşmasını nümayəs etdirir. Layihənin əsas məqsədi, mərkəzləşdirilmiş idarəetmə və avtomatlaşdırma vasitəsilə kiber-təhdidlərin aşkarlanması prosesini optimallaşdırmaqdır.

---

## 🏗️ Memarlıq və Komanda İş Bölgüsü
Layihə SOC (Security Operations Center) əməliyyatlarının fərqli istiqamətlərini əhatə edən birgə əməkdaşlıq məhsuludur:

* **Komanda Yoldaşı (Splunk Mütəxəssisi):** - 15 mürəkkəb analitik qaydanın yaradılması.
    - **SPL** (Splunk Processing Language) sorğularının optimallaşdırılması.
    - **MTTD** (Aşkarlama Sürəti) və **MTTR** (Reaksiya Sürəti) dashboard-larının qurulması.
* **Mən (QRadar & Avtomatlaşdırma Mühəndisi):** - 10 professional korrelyasiya qaydasının (Correlation Rules) qurulması.
    - **REST API** vasitəsilə qaydaların avtomatik tətbiqi (GitHub Sync).
    - Windows Server log siyasətinin (**GPO**) tənzimlənməsi.

---

## 🛡️ Aşkarlama Strategiyası (MITRE ATT&CK Mapping)
Aşkarlama strategiyamız kiber-hücum zəncirinin bütün mərhələlərini əhatə edir. Implementasiya olunmuş 25+ qayda aşağıdakı kateqoriyalara bölünür:

| Platforma | Kateqoriya | Qayda Sayı | Əsas Texnikalar (Techniques) |
| :--- | :--- | :--- | :--- |
| **Splunk** | Analytics & Hunting | 15 | Anomalous Network Traffic, User Behavior (UBA) |
| **QRadar** | Correlation & Persistence | 10 | Golden Ticket, LSASS Dumping, LOLBins (Certutil) |

### 📂 Seçilmiş Professional Qaydalar (QRadar)
1.  **Rule 1: Brute Force Success** (T1110)
2.  **Rule 2: Golden Ticket Detection** (T1558.001)
3.  **Rule 4: Certutil Web Download** (T1105)
4.  **Rule 5: LSASS Memory Dumping** (T1003.001)
5.  **Rule 9: Clear Event Logs** (T1070.001)

---

## ⚙️ Avtomatlaşdırma və İnteqrasiya (API Deployment)
Təhlükəsizlik qaydalarına bir "kod" (Detection as Code) kimi yanaşılır. Əllə konfiqurasiya əvəzinə sistem aşağıdakı kimi işləyir:
* **Automation:** Python skripti **Authorized Service Token** vasitəsilə GitHub-dakı qaydaları **REST API** üzərindən birbaşa QRadar-a yükləyir.
* **Source of Truth:** GitHub bütün aşkarlama məntiqləri üçün mərkəzi anbar rolunu oynayır.

---

## 🛡️ Log Siyasəti və Optimallaşdırma (Logging Policy)
Yüksək dəqiqlikli xəbərdarlıqlar (High-fidelity alerts) əldə etmək və SIEM performansını qorumaq üçün:
* **Advanced Audit Policy:** Domain Controller üzərində xüsusi **GPO** (Group Policy) tətbiq edilib.
* **Filtering:** Yalnız kritik loglar (Process Creation, Account Management, Object Access) SIEM-ə yönləndirilir. Client cihazların logları mənbədə süzülür.

---

## 📊 Performans Metrikləri (KPI)
Sistem aşağıdakı SOC metriklərini real vaxt rejimində ölçür:
* **MTTD (Mean Time to Detect):** Hadisə baş verdikdən alarm yaranana qədər keçən orta vaxt.
* **MTTR (Mean Time to Respond):** Alarm yarandıqdan insident bağlanana qədər keçən orta vaxt.

---

### 🚀 Gələcək Təkmilləşdirmələr
- **SOAR** (Security Orchestration, Automation, and Response) inteqrasiyası.
- **Threat Intelligence** feed-lərin avtomatik daxil edilməsi.
