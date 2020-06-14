#Carlos Trejos Elizondo   2018132777

#Abre el archivo de texto, el archivo se llama: texto.txt
f=open('textoEntrada.txt','r')
text=f.read()
f.close
#Funcion menu para escoger la funcion a realizar
def main():
    done=False
    while not done:
        print()
        print('# # # # # # # #')
        print('     Menú     ')
        print('# # # # # # # #')
        print('1. Encriptar.')
        print('2. Desencriptar.')
        print('0. Salir.')
        print()
        opc=input('Digite la opción: ')
        if opc == '1':
            llave=int(input('Digite la llave: '))
            if llave < 255:
                enc(llave)
            else:
                print('La llave debe ser menor a 255')
        elif opc == '2':
            llave=int(input('Digite la llave: '))
            if llave < 255:
                des(llave)
            else:
                print('La llave debe ser menor a 255')
        elif opc == '0':
            return
        else:
            print('Opción inválida.')
            input('Presione enter para continuar.')
    
#"enc" funcion que llama la axiliar con mas parametros, la funcion auxiliar
#es la que realiza la encriptacion del texto y tambien llama la funcion "key"
#para generar otra llave
def enc(llave):
    return encaux(text+' ',llave,0,0,'')
    
def encaux(text,llave,i,e,res):
    abc=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z']
    cona=abc[i]
    con=text[e]
    if cona==con:
        p=abc[i+llave]
        res=res+p
        llave=key(llave)
        return encaux(text,llave,i-i,e+1,res)
    elif e+1==len(text):
        return esc(res)
    elif con==' ':
        res=res+' '
        return encaux(text,llave,i-i,e+1,res)
    else:
        return encaux(text,llave,i+1,e,res)
    
#"key" es la funcion que genera las llaves, esta solo cambia el numero a binario y llama la auxiliar
def key(llave):
    bi=bin(llave)[2:]
    if bi==0:
        return 0
    else:
        return keyau(bi,[])
    
#"keyau" es la funcion auxiliar de key, es donde se genera la lista del numero binario y aplica los
#xor a las respectivas posiciones, llama otra la funcion dec
def keyau(bi,biL):
    if len(biL)==8:
        biL=[0]+biL
        biL[0]=biL[8]^biL[6]^biL[4]^biL[3]
        biL=biL[:8]
        p=biL[0]*10**7+biL[1]*10**6+biL[2]*10**5+biL[3]*10**4+biL[4]*1000+biL[5]*100+biL[6]*10+biL[7]
        return dec(str(p))
    elif bi==0:
        return keyau(bi,[0]+biL)
    else:
        bi=int(bi)
        temp=bi%10
        return keyau(bi//10,[temp]+biL)

#La funcion "dec" pasa el nuevo numero binario a decimal
def dec(binario,i=0):  
    n=len(binario)  
    if (i==n-1): 
        return int(binario[i])-0
    else:
        return(((int(binario[i])-0)<<(n-i-1))+dec(binario,i+1))

#La funcion des descencriptan el texto con la llave inicial que se brindo
    #al encriptar
def des(llave):
    return desaux(text+' ',llave,0,0,'')

def desaux(text,llave,i,e,res):
    abc=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z']
    cona=abc[i]
    con=text[e]
    if cona==con:
        p=abc[i-llave]
        res=res+p
        llave=key(llave)
        return desaux(text,llave,i-i,e+1,res)
    elif e+1==len(text):
        return esc(res)
    elif con==' ':
        res=res+' '
        return desaux(text,llave,i-i,e+1,res)
    else:
        return desaux(text,llave,i+1,e,res)

#Funcion para generar un archivo txt con el texto encriptado o desencriptado
def esc(res):
    f = open ('textoSalida.txt','w+')
    f.write(res)
    f.close()
    print('Documento creado exitosamente')
    
main()
