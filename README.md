# U04_DS_IndirectGroupCommunication

Para poder habilitar multiples conexiones de clientes diferentes he tenido que modificar el programa client_sub.py.

1. El problema a la hora de conectar multiples clientes es, que en el momento de realizar el bind() del socket de una segunda conexión de cliente saltaba una excepción debido a que el puerto que estabamos utilizando era el mismo que se había utilizado en la conexión anterior, la solución ha sido volver a intentar a realizar el bind() con el siguiente puerto vacío y para ello le he ido sumando uno al puerto hasta encontrar uno que no estuviera siendo utilizado. Con esto ya ha sido posible conectar multiples conexiones con el broker.

2. No obstante ha sido necesario otro cambio en el código de client_sub.py ya que en el momento de realizar una publicación ejecutando client_pub.py, este solo lo recibía el broker y la primera conexión que se había establecido, y eso era debido a que de la forma que estaba estructurado el código, primero se enviaba un mensaje con la dirección del socket al broker para suscribirnos y luego mirabamos si el puerto estaba siendo usado, por lo que el broker de todas las conexiones recibía siempre la dirección con el mismo puerto en vez de ir recibiendo el puerto con el incremento realizado en el paso 1.
