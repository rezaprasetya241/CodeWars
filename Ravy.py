class buku:
    def __init__(self, judul, pengarang):
        self.judul = judul
        self.pengarang = pengarang
    def display(self):
        print("Buku ini berjudul " + self.judul + " Dengan pengarang " + self.pengarang)

buku1 = buku("Mudah Belajar Python", "Alex Komputindo")
buku1.display()