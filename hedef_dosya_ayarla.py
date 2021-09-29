import os
def hedef_dosya_ayarla(hedef_dosya):
    """Parametre olarak alinan dosyanin bilgisayardaki konumunu doner."""
    dosya_yolu = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(dosya_yolu, hedef_dosya)
    
    
