from Guiao2.productClasses import Produt, Livro, Telemovel, Televisor, Electrodomestico
 

def teste():

    livro1 = Livro("Livro 1",100, 15.0) # nome, stock, preço
    livro1.add_autor("Autor 1")
    livro1.add_autor("Autor 2")
    print(f"{livro1.get_nome()} tem {len(livro1.get_autores())} autores");
		
    lista = []
    lista.append("Autor X"); lista.append("Autor Y")
    lista.append("Autor Z")
		
    livro2 = Livro("Livro 2",0,23.0, lista)
    livro2.add_stock(450);
    print(f"{livro2.get_nome()} tem {livro2.get_num_autores()}  autores");

    tlv1 = Televisor("Sony","KX1188",3,1000,56)  # marca, modelo, stock, preco, polegadas

    tlm1 = Telemovel("XWZ","Model A", 10, 560.0 ); # marca, modelo, quantidade, preço

    electr1 = Electrodomestico("Frigorífico", 2, 780);
    electr2 = Electrodomestico("Fogão" , 1, 423);
    electr1.set_classe("A+"); 
		
    #  adicionar a lista com produtos na loja
    lista_produtos = []
    lista_produtos.append(livro1); lista_produtos.append(livro2); 
    lista_produtos.append(electr1); lista_produtos.append(electr2);
    lista_produtos.append(tlm1); lista_produtos.append(tlv1);
	    
    tlm1.add_stock(3);

	# lista todos os produtos, com preços, numa tabela		 		
    print("Lista de Todos os Produtos:");

    for prod in lista_produtos:
        print(prod)


if __name__ == "__main__":
    teste()