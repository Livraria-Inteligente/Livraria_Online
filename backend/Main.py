class livro:
    
    def __init__(self, titulo, autor, ano_publicacao, estado):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.estado = estado


class usuario:
    
    def __init__(self, nome, id, livros_emprestados):
        self.nome = nome
        self.id = id
        self.livros_emprestados = livros_emprestados



class biblioteca:
    
    def __init__(self, adicionar, listar, emprestar,devolver):
        self.adicionar = adicionar
        self.listar = listar
        self.emprestar = emprestar
        self.devolver = devolver
        
        
    def pegar_livros(self, livro):
        self.livros_emprestados.append(livro)
         
        
        
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        