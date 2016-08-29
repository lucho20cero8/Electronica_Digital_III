;EL siguiente programa verifica la paridad del
;numero contenido en el registro dx imprimiendo en pantalla
;0 para numero par y
;1 para numero impar.


.model small
.data
 DATO DB 0
.code 


	sub ax,ax	;Inicializacion registro ax
	mov dx,10h 	;Numero a verificar
	and dl,1h
	mov al,dl
	add ax,30h	;Para convertir numero a ASCII
	mov si,200h
	mov [si],al
	inc si
	mov bl,24h	;24H equivale en ascii: $
	mov [si],bl
	
	;Fragmento para imprimir en pantalla
	mov dx,200h	;Punto de partida para imprimir
	mov ah,09h	;FunciÛn 9h
	int 21h		;InterrupciÛn 21


MOV Ah, 4Ch 		; volver al DOS
INT 21h			;InterrupciÛn 21H

end
