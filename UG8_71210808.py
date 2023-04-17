from collections import deque

class Kasir:
    def __init__(self):
        self.queue = deque()
    
    def __len__(self):
        return len(self.queue)
    
    def is_empty(self):
        return len(self.queue) == 0
    
    def dequeue(self):
        if not self.is_empty():
            return self.queue.popleft()
    
    def enqueue(self, pelanggan):
        self.queue.append(pelanggan)
        
    def printAll(self):
        print("=== Kasir ===")
        for i in range(len(self.queue)):
            print(f"{i+1}. {self.queue[i]}")

kasir = Kasir()

kasir.enqueue("Haniif")
kasir.enqueue("Sindu")
kasir.enqueue("Dedi")

kasir.printAll()

print("Pelanggan Haniif Selesai Membayar")
kasir.dequeue()

print("*** Melakukan Resize ***")
kasir.enqueue("Beatrix")
kasir.enqueue("Kosong")
kasir.enqueue("Kosong")
kasir.printAll()

print("Pelanggan Sindu Selesai Membayar")
kasir.dequeue()
kasir.printAll()
kasir.enqueue("Shalon")
kasir.printAll()
