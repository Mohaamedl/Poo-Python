from Guiao2.productClasses import Book, Phone, Television, HomeAppliance
 

def teste():

    livro1 = Book("Livro 1",100, 15.0) # nome, stock, preço
    livro1.addAuthor("Autor 1")
    livro1.addAuthor("Autor 2")
    print(f"{livro1.getName()} tem {len(livro1.getAuthors())} autores")
		
    lista = []
    lista.append("Autor X"); lista.append("Autor Y")
    lista.append("Autor Z")
		
    livro2 = Book("Livro 2",0,23.0, lista)
    livro2.addStock(450)
    print(f"{livro2.getName()} tem {livro2.getNumAuthors()}  autores")

    tlv1 = Television("Sony","KX1188",3,1000,56)  # marca, modelo, stock, preco, polegadas

    tlm1 = Phone("XWZ","Model A", 10, 560.0 ); # marca, modelo, quantidade, preço

    electr1 = HomeAppliance("Frigori",'LG','FDE4', 2, 780)
    electr2 = HomeAppliance("Fogão",'LG','7GT' , 1, 423)
    electr1.setClasse("A+"); 
		
    #  adicionar a lista com produtos na loja
    lista_produtos = []
    lista_produtos.append(livro1); lista_produtos.append(livro2); 
    lista_produtos.append(electr1); lista_produtos.append(electr2)
    lista_produtos.append(tlm1); lista_produtos.append(tlv1)
	    
    tlm1.addStock(3)

	# lista todos os produtos, com preços, numa tabela		 		
    print("Lista de Todos os Produtos:")
    print('id       nome                    stock     preço  preço ao cliente')

    for prod in lista_produtos:
        print(prod)


if __name__ == "__main__":
    teste()