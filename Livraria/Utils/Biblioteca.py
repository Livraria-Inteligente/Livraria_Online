
class biblioteca:
    
    def __init__(self, adicionar, listar, emprestar,devolver):
        self.adicionar = adicionar
        self.listar = listar
        self.emprestar = emprestar
        self.devolver = devolver
        
        
    def pegar_livros(self, livro):
        self.livros_emprestados.append(livro)
         
        
        