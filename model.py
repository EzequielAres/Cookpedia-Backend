from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy_utils import database_exists

# instantiate SQLAlchemy object
db = SQLAlchemy()


def init_db(app, guard, testing=False):
    """
    Initializes database

    :param testing:
    :param app: flask app
    :param guard: praetorian object for password hashing if seeding needed
    """
    db.init_app(app)
    if testing or not database_exists(app.config['SQLALCHEMY_DATABASE_URI']):
        # if there is no database file
        # migrate model
        db.create_all(app=app)
        # seed data
        seed_db(app, guard)


# Seeder aplicación
def seed_db(app, guard):
    with app.app_context():

        usuarios = [
            Usuario(nombre="Ezequiel", nick="Zzequi", email="ezequiel@gmail.com",
                    hashed_password=guard.hash_password("pestillo"), imagen="http://localhost:5000/static/usuarios"
                                                                            "/anon.jpg", is_admin=True),
            Usuario(nombre="Ana", nick="Anita", email="ana@gmail.com",
                    hashed_password=guard.hash_password("pestillo"), imagen="http://localhost:5000/static/usuarios"
                                                                            "/anon.jpg", is_admin=False),
            Usuario(nombre="Paco", nick="Pakito", email="paco@gmail.com",
                    hashed_password=guard.hash_password("pestillo"), imagen="http://localhost:5000/static/usuarios"
                                                                            "/anon.jpg", is_admin=True),
            Usuario(nombre="María", nick="Marieta", email="maria@gmail.com",
                    hashed_password=guard.hash_password("pestillo"), imagen="http://localhost:5000/static/usuarios"
                                                                            "/anon.jpg", is_admin=False),
            Usuario(nombre="Alejandro", nick="Alex", email="alex@gmail.com",
                    hashed_password=guard.hash_password("pestillo"), imagen="http://localhost:5000/static/usuarios"
                                                                            "/anon.jpg", is_admin=True)
        ]

        ingredientes = [
            Ingrediente(nombre="Galletas"),
            Ingrediente(nombre="Mantequilla"),
            Ingrediente(nombre="Yogur natural"),
            Ingrediente(nombre="Nata"),
            Ingrediente(nombre="Limón"),
            Ingrediente(nombre="Hoja gelatina"),
            Ingrediente(nombre="Azúcar"),
            Ingrediente(nombre="Agua"),
            Ingrediente(nombre="Arroz"),
            Ingrediente(nombre="Leche"),
            Ingrediente(nombre="Canela"),
            Ingrediente(nombre="Cáscara de limón"),
            Ingrediente(nombre="Pan de molde"),
            Ingrediente(nombre="Huevos (M)"),
            Ingrediente(nombre="Carne picada"),
            Ingrediente(nombre="Sal de ajo"),
            Ingrediente(nombre="Hierbas provenzales"),
            Ingrediente(nombre="Ketchup"),
            Ingrediente(nombre="Mostaza de Dijon"),
            Ingrediente(nombre="Sal"),
            Ingrediente(nombre="Pimienta negra molida"),
            Ingrediente(nombre="Aceite de oliva"),
            Ingrediente(nombre="Harina de fuerza"),
            Ingrediente(nombre="Sal fina"),
            Ingrediente(nombre="Levadura fresca"),
            Ingrediente(nombre="Tomate pera"),
            Ingrediente(nombre="Tomate rama"),
            Ingrediente(nombre="Pimiento verde"),
            Ingrediente(nombre="Cebolleta"),
            Ingrediente(nombre="Pepino"),
            Ingrediente(nombre="Diente de ajo"),
            Ingrediente(nombre="Huevo cocido"),
            Ingrediente(nombre="Vinagre"),
            Ingrediente(nombre="Patatas monalisa"),
            Ingrediente(nombre="Zanahoria"),
            Ingrediente(nombre="Aceitunas"),
            Ingrediente(nombre="Guisantes cocidos"),
            Ingrediente(nombre="Atún en aceite"),
            Ingrediente(nombre="Mayonesa"),
            Ingrediente(nombre="Zumo de limón"),
            Ingrediente(nombre="Rape"),
            Ingrediente(nombre="Harina"),
            Ingrediente(nombre="Aceite para freir"),
            Ingrediente(nombre="Canela en polvo"),
            Ingrediente(nombre="Agua con sal"),
            Ingrediente(nombre="Berberechos frescos"),
            Ingrediente(nombre="Tomates maduros"),
            Ingrediente(nombre="Pimiento choricero"),
            Ingrediente(nombre="Rebanada de pan"),
            Ingrediente(nombre="Almendras"),
            Ingrediente(nombre="Avellanas"),
            Ingrediente(nombre="Cabeza de ajo"),
            Ingrediente(nombre="Mantequilla sin sal"),
            Ingrediente(nombre="Chocolate negro"),
            Ingrediente(nombre="Azúcar moreno"),
            Ingrediente(nombre="Harina de trigo"),
            Ingrediente(nombre="Almendras molidas"),
            Ingrediente(nombre="Levadura química"),
            Ingrediente(nombre="Bicarbonato sódico"),
            Ingrediente(nombre="Leche entera"),
            Ingrediente(nombre="Chips de chocolate"),
            Ingrediente(nombre="Patatas"),
            Ingrediente(nombre="Lubinas"),
            Ingrediente(nombre="Guindillas cayena"),
            Ingrediente(nombre="Perejil"),
            Ingrediente(nombre="Espagueti"),
            Ingrediente(nombre="Queso curado"),
            Ingrediente(nombre="Bacon"),
        ]

        recetas = [
            Receta(nombre="Tarta de limón sin queso", descripcion="La tarta de limón sin queso es una elaboración "
                                                                  "deliciosa, fresquita y sencilla de preparar. Un "
                                                                  "pastel de limón ideal para después de una comida, "
                                                                  "ya que es ligero y con un sabor agradable. Además, "
                                                                  "esta receta que os presentamos no contiene queso, "
                                                                  "se elabora con yogur y con nata. Por otro lado, "
                                                                  "no necesita horno y es ideal para el verano. Sin "
                                                                  "embargo, aunque no necesite horno, si es necesario "
                                                                  "3-4 horas para que esté la tarta fría, incluso, "
                                                                  "el día siguiente está más buena.",
                   imagen="https://images.pexels.com/photos/8942530/pexels-photo-8942530.jpeg?auto=compress&cs"
                          "=tinysrgb&w=1260&h=750&dpr=1", video="", pasos="Para empezar con la receta de tarta de "
                                                                          "limón sin queso, primero debes preparar la "
                                                                          "base de la tarta. Para ello, tritura las "
                                                                          "galletas y derrite la mantequilla. "
                                                                          "Incorpora la mantequilla junto con las "
                                                                          "galletas y amasa hasta que los dos "
                                                                          "ingredientes queden bien integrados. "
                                                                          "\n Cubre el fondo de un molde de 20 cm con "
                                                                          "la masa de galletas. A continuación, "
                                                                          "aplasta bien con "
                                                                          "ayuda de una cuchara para que quede bien "
                                                                          "compacta y uniforme la base. Mientras, "
                                                                          "reserva en la nevera. "
                                                                          "\n En un bol con agua fría pon en remojo "
                                                                          "las hojas de gelatina. "
                                                                          "\n Exprime los limones y, si te gusta más "
                                                                          "sabor a limón, puedes añadir también la "
                                                                          "ralladura de los mismos. "
                                                                          "\n En un bol añade el zumo de los 2 "
                                                                          "limones, el azúcar y dos cucharadas de "
                                                                          "agua. A continuación, introduce en el "
                                                                          "microondas unos segundos para que esté "
                                                                          "caliente. Cuando estén las hojas de "
                                                                          "gelatina hidratadas, escúrrelas bien y "
                                                                          "añade en el zumo de limón que estará "
                                                                          "caliente. Enseguida, remueve bien para que "
                                                                          "quede bien desecho. "
                                                                          "\n Por otro lado, vierte la crema de leche "
                                                                          "y bate hasta que quede la nata montada. "
                                                                          "Incorpora la crema anterior en el bol de "
                                                                          "la nata y mezcla bien todo. ¡Te encantará "
                                                                          "esta tarta de limón y nata! "
                                                                          "\n Cuando vayas a servir la deliciosa "
                                                                          "tarta de limón sin horno, retira de la "
                                                                          "nevera, desmolda y colócala en un plato. "
                                                                          "Si lo prefieres, puedes acompañar esta "
                                                                          "tarta con frutas de temporada. ¡A comer! "
                                                                          "Cuéntanos en los comentarios tu opinión y "
                                                                          "comparte con nosotros una fotografía del "
                                                                          "resultado final.", id_usuario=1),

            Receta(nombre="Arroz con leche", descripcion="Hay postres que son todo un clásico de nuestra repostería y "
                                                         "uno de ellos sin duda es el arroz con leche. Diría que lo "
                                                         "tiene todo porque se utilizan ingredientes que solemos "
                                                         "tener en casa, se prepara de una forma muy sencilla, "
                                                         "se puede utilizar la cantidad de dulzor que se desee sin "
                                                         "que la textura se vea afectada y, por supuesto, "
                                                         "está buenísimo.", imagen="https://st.depositphotos.com"
                                                                                   "/2461721/2717/i/450"
                                                                                   "/depositphotos_27175187-stock"
                                                                                   "-photo-rice-pudding-top-view.jpg",
                   video="", pasos="Pon la mariposa en las cuchillas y vierte en el vaso de la Thermomix la leche, la piel de limón y las ramas de canela. Calienta durante 10 minutos a 90ºC y velocidad 1."
                         "\n Incorpora el arroz y cocina durante 30 minutos a 90ºC y velocidad 1."
                         "\n Añade el azúcar y sigue cocinando durante 10 minutos a 90ºC y velocidad 1. "
                         "\n Prueba el arroz y, si los granos están hechos (ya no se notan crudos) y la textura es la que más te gusta, quita las ramas de canela y la cáscara de limón y échalo en los recipientes en los que vayas a servirlo (pueden ser 4 raciones abundantes o 6 un poco más pequeñas) para que termine de asentarse."
                         "\n Puede consumirse al momento, templadito, aunque normalmente es un postre que suele gustar frío así que deja que se enfríe en los recipientes y cuando esté totalmente frío déjalo en la nevera hasta el momento de consumir, diría que mínimo un par de horas de nevera para que esté fresquito."
                         "\n Espolvorea con canela por encima o bien carameliza su superficie. Para ello puedes echar una cucharadita de azúcar encima del arroz bien repartida y con la ayuda de un soplete ir derritiendo el azúcar para que se forme una costra encima del arroz que cuando se enfríe estará crujiente. ¡Delicioso! ",
                   id_usuario=1),

            Receta(nombre="Hamburguesa",
                   descripcion="Qué ricas son las hamburguesas, ¿verdad? A mí me encantan y me resultan una comida muy equilibrada, muy fácil y muy rápida de preparar. Hace años que las preparo de la misma manera y no me planteo cambiarla. Porque después de probar muchas variantes, esta es mi mejor receta de hamburguesa. Y es que, si algo funciona, mejor dejarlo tal cual. ",
                   imagen="https://images.pexels.com/photos/3219483/pexels-photo-3219483.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
                   video="http://localhost:5000/static/recetas/Hamburguesa.webm",
                   pasos="\n En un recipiente hondo mezclamos la leche con el huevo, el ketchup, la mostaza, la sal de ajo, las hierbas provenzales y salpimentamos al gusto. Batimos e incorporamos las dos rebanadas de pan de molde troceadas. Aplastamos con un tenedor para que el pan se empape bien al tiempo que hacemos una masa lo más parecida posible a una papilla en la que no se noten trozos de pan."
                         "\n Agregamos la carne picada y, con las manos bien limpias, mezclamos hasta incorporar bien. Dividimos la mezcla de nuestras hamburguesas en seis partes iguales. Tomamos cada una de ellas, la boleamos y la aplastamos entre las palmas de las manos. Podemos usar un aro de emplatar o algún artilugio para formar hamburguesas, pero no es necesario."
                         "\n Pincelamos una sartén amplia o una plancha con aceite de oliva y la calentamos a fuego fuerte. Colocamos sobre ella las hamburguesas y las marcamos, sin tocar ni aplastar, durante dos o tres minutos, bajando el fuego a media cocción. Volteamos, cubrimos cada hamburguesa con dos lonchas de queso, tapamos y dejamos cocer por la otra cara durante otros dos o tres minutos minutos. El tiempo dependerá del punto que queramos darle a la carne. Servimos inmediatamente.",
                   id_usuario=1),

            Receta(nombre="Huevo frito",
                   descripcion="En casa nos gustan los huevos preparados de cualquier forma y raro es el día que no los tomamos, sobre todo en el desayuno cocidos o poché aunque también nos encantan los huevos revueltos, las tortillas y por supuesto fritos que es como los voy a preparar en esta receta. Ya sean los protagonistas del plato o un componente más, siempre dan un toque increíble a todo lo que tocan. "
                               "\n Aprende cómo hacer un huevo frito perfecto, con trucos y consejos muy sencillos para conseguir el mejor resultado, que no es ni más ni menos que un huevo frito a tu gusto, te guste como te guste. Con la yema líquida o cuajada, con o sin puntilla, cocinados con más o menos aceite… hay muchos detalles que elegir. ",
                   imagen="https://images.pexels.com/photos/5092568/pexels-photo-5092568.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
                   video="http://localhost:5000/static/recetas/huevo.webm",
                   pasos="Para freír huevos lo ideal es contar con una sartén antiadherente que no se pegue nada y una espumadera. Si tu sartén lleva una capa de antiadherente, para no rallarlo deberás utilizar una espumadera no sea metálica. En mi caso estoy utilizando una sartén de hierro en la que, cuando cocino con la base de aceite, no se pega nada (esto es porque es bastante nueva, conforme la vaya usando y se ponga más negra, más antiadherente será). Su base mide 14 cm y las paredes se extienden hasta los 20 cm."
                         "\n Puedes utilizar una sola sartén justa para un huevo o bien varias sartenes individuales o bien una sartén grande para freír varios huevos a la vez.",
                   id_usuario=2),

            Receta(nombre="Pizza casera",
                   descripcion="Elaborar nuestra propia receta de pizza casera fácil es un proceso mucho más sencillo de lo que creemos, solo necesitamos conocer los ingredientes para pizza necesarios y el proceso a seguir para integrarlos. En RecetasGratis queremos que aprendas recetas fáciles que te permitan preparar platos exquisitos y únicos, como diferentes variedades de pizzas caseras. Por ello, aquí te mostramos cómo hacer pizza casera, ¿vas a perdértela?",
                   imagen="https://images.pexels.com/photos/708587/pexels-photo-708587.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
                   video="",
                   pasos="\n Antes de empezar con la receta de pizza casera fácil resulta fundamental hacer una pequeña aclaración sobre la harina. Para realizar este tipo de masas, la harina más recomendada es la de fuerza, puesto que al contener un mayor porcentaje de gluten el resultado será una masa de pizza casera mucho más esponjosa. En los países de América Latina, sobre todo, este tipo de harina es conocido como harina 00. Ahora bien, si quieres hacer pizza casera sin gluten, consulta esta otra receta."
                         "\n Ahora sí, ¡empezamos la receta de pizza casera! Para ello, lo primero que vamos a hacer es mezclar en un recipiente el agua templada con la levadura fresca. Para elaborar una masa para pizza casera fácilmente puedes utilizar este tipo de levadura o hacer una masa de pizza con levadura seca, ambas son válidas. En el caso de que prefieras la seca, deberás mezclarla con la harina y si, por el contrario, prefieres la fresca, es fundamental mezclarla con agua tibia. La levadura fresca es aquella que se vende en bloque y se tiene que conservar en el frigorífico."
                         "\n En general, unos 30 gramos de levadura fresca equivalen a unos 10 gramos de levadura seca, tenlo en cuenta por si quieres usar una levadura diferente a la de esta receta de pizza italiana."
                         "\n Cuando hayas mezclado la levadura con el agua, agrega las dos cucharadas de aceite. Mezcla bien para que se integren todos los ingredientes para la pizza."
                         "\n Antes de que la preparación se enfríe, añade en un bol amplio la harina de fuerza y la sal, acomódalas en forma de volcán. Vierte la mezcla anterior en el centro."
                         "\n Ahora es cuando tienes que empezar a amasar bien hasta que notes que la masa de pizza casera deja de pegarse en tus manos y puedes manejarla sin problemas."
                         "\n Cuando tengas la masa de pizza esponjosa lista, deberás darle forma de tubo largo y cortarla en 4 particiones. Después, haz una bola con cada partición y tápalas con un trapo limpio y seco. Deberás dejarlas reposar durante 45 minutos. Verás que, poco a poco, empiezan a elevarse hasta duplicar su volumen. Cada bola de masa te servirá para hacer una pizza casera normal."
                         "\n Pasado el tiempo correspondiente, espolvorea un poco de harina sobre una mesa para preparar la pizza casera, coge una de las bolas y colócala sobre ella. Ahora deberás extenderla con tus manos estirando desde el centro hacia los costados, dándole forma circular. Si dispones de rodillo también puedes utilizarlo para que quede más fina la masa. Una vez estirada, ya puedes añadir la salsa para pizza casera y los ingredientes para pizza que prefieras. Puedes usar esta deliciosa receta casera de salsa de tomate y cebolla para pizza."
                         "\n Una vez hayas escogido los ingredientes y tengas tu masa de pizza casera terminada, deberás precalentar el horno a temperatura máxima durante unos 20 minutos."
                         "\n Pasado el tiempo, introduce la preparación pizza casera y hornéala durante 10 minutos aproximadamente. Deberás vigilarla porque el tiempo final variará en función del tipo de horno y la intensidad que tenga. ¡Listo, tu pizza casera al horno estará para chuparse los dedos!",
                   id_usuario=2),

            Receta(nombre="Gazpacho",
                   descripcion="El gazpacho andaluz es una receta tradicional andaluza que junto al salmorejo o el ajoblanco apetece a cualquier hora en verano. Se puede mantener fresco en la nevera y tenerlo listo para comer o cenar del día anterior. Cuanto más fresquito mejor. Lo podemos tomar sólo o acompañarlo de una brunoise de las hortalizas con las que lo hacemos y huevo cocido, a gusto del comensal. Normalmente se utilizan tomates de la variedad pera pero se pueden mezclar con tomates rama que dan más sabor a la receta.",
                   imagen="https://images.pexels.com/photos/8796313/pexels-photo-8796313.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
                   video="",
                   pasos="La receta del gazpacho es muy sencilla. Lo primero que hay que hacer es lavar bien las verduras y trocearlas. Para el gazpacho utilizaremos todos los tomates (menos 1 de rama que reservaremos para la guarnición), tres cuartos de pepino (si no es muy grande), media cebolleta, medio pimiento verde, medio diente de ajo sin el germen, aceite de oliva virgen extra, vinagre y sal. El pepino lo pelamos antes de trocear y añadir a los demás ingredientes. Se aliñan los ingredientes con el aceite de oliva virgen extra, el vinagre y la sal. Si la batidora que se utilizará para triturar los ingredientes es muy potente se pueden dejar los tomates con la piel. Si no, podemos escaldarlos y quitarles la piel previamente. Se puede utilizar una batidora de vaso, un robot de cocina o la batidora de mano de toda la vida que conocemos para triturar los ingredientes. Si vemos que queda muy espeso añadimos una pizca de agua aunque lo ideal es no añadir agua. Lo reservamos en la nevera que esté bien fresquito mientras se prepara la guarnición.",
                   id_usuario=2),

            Receta(nombre="Ensaladilla rusa",
                   descripcion="Pues sí, la ensaladilla rusa es casi casi de origen ruso. En concreto fue Lucien Olivier, un cocinero franco-belga, quien la cocinó para la élite de la capital rusa usando ingredientes tan exuberantes como caviar o lengua aunque antes, ya se cocinaban otras ensaladillas parecidas por Europa, también con ingredientes lujosos como la langosta. Así, a mediados del siglo XIX aparece en Francia una versión con patatas y mayonesa como ingredientes principales, ingredientes más populares.",
                   imagen="https://images.pexels.com/photos/4210803/pexels-photo-4210803.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
                   video="",
                   pasos="Comenzamos poniendo 2 patatas de la variedad Monalisa lavadas, y enteras con la piel, y una zanahoria limpia en agua fría salada en una olla. Llevaremos la olla al fuego y cocinaremos las patatas y la zanahoria durante unos 35 minutos a fuego medio."
                         "\n Transcurridos los 35 minutos añadimos 1 huevo y dejamos que hierva todo junto otros 10 minutos. \n Retiramos las patatas, la zanahoria y el huevo del agua de cocción, y dejamos que se enfríen antes de pelarlo todo."
                         "\n Cortamos en trozos pequeños las patatas, la zanahoria y el huevo. Si hemos elegido aceitunas con hueso cortaremos 50 gramos de manera que nos quedemos solo con la carne de las aceitunas desechando el hueso. Si por el contrario elegimos aceitunas sin hueso, troceamos directamente 50 gramos de estas aceitunas."
                         "\n En un bol ponemos las patatas, la zanahoria, el huevo y las aceitunas junto con 75 g de guisantes cocidos y escurridos de su líquido y 150 g de atún en aceite también escurrido de este."
                         "\n Añadimos al bol 400 g de mayonesa, que puede ser mayonesa casera o bien una buena mayonesa comercial."
                         "\n Mezclamos todos los ingredientes muy bien. No hay que preocuparse si la patata se deshace un poco ya que esto dará como resultado una buena ensaladilla rusa, muy cremosa. Llevamos la ensaladilla a la nevera y la servimos fría acompañada de unos picos de pan.",
                   id_usuario=3),

            Receta(nombre="Salsa alioli",
                   descripcion="Una de las salsas más típicas de nuestra gastronomía, la salsa de alioli casera, que viene de all-i-oli (ajo y aceite, sus dos ingredientes básicos). Acompaña gran diversidad de platos, como los asados de carne, las clásicas patatas con ajo, en ensaladas de verano, con carnes y pescados, con arroz… vamos, que tienes que aprender a hacerla ya porque vas a poder incorporarla a un montón de platos. Esta receta de alioli la hago con batidora porque así es más difícil que se te pueda cortar la salsa. ",
                   imagen="https://st2.depositphotos.com/1364913/7108/i/450/depositphotos_71089381-stock-photo-garlic-dip-top-view.jpg",
                   video="",
                   pasos="Empezamos con un truco: si quieres un alioli que no repita y de sabor un poco más suave, introduce el ajo unos 10 segundos en el microondas o cuécelo 2 minutos en agua hirviendo, y utilízalo para preparar el alioli."
                         "\n En el vaso de la batidora, introduce los dientes de ajo, el huevo crudo, la sal, el aceite y el zumo de limón."
                         "\n Deberás colocar la batidora en el fondo del vaso, totalmente plana, y empezar a batir sin moverla en absoluto."
                         "\n Cuando notes que empiece a emulsionar la salsa por la parte inferior (significa que empieza a espesarse), eleva el brazo de la batidora hacia arriba y hacia abajo, con movimientos suaves, hasta que toda la salsa quede espesa y homogénea, sin grumos ni restos de ingredientes.",
                   id_usuario=3),

            Receta(nombre="Fritos de rape",
                   descripcion="Omnipresentes junto al chorizo a la sidra o los escalopines al cabrales, pocas son las sidrerías o casas de yantar que no ofrezcan los fritos de pixín, que es como se conoce al rape en el principado. Se trata de una receta asturiana muy popular y se prepara de una manera muy sencilla pues, en resumen, es rape troceado, rebozado y, como su nombre indica, frito. Nada más. Por ello, cabe destacar que, para que nos quede de lujo, se necesita un buen producto, un pescado fresco que conserve todo su buen sabor.",
                   imagen="https://imag.bonviveur.com/fritos-de-rape-o-de-pixin.webp",
                   video="",
                   pasos="Para preparar nuestros fritos de rape, vamos a necesitar 400 g de rape sin espinas, bien en colas o en rodajas, según preferencias. Cortamos el rape en trozos del tamaño de uno o dos bocados, al gusto."
                         "\n Opcionalmente, podemos macerar el pescado. Para ello, tomamos 1 diente de ajo, lo pelamos y lo cortamos en láminas o lo picamos. Ponemos el pescado en un bol y lo mezclamos con el ajo y 1 chorrito de zumo de limón. No necesita mucho. Dejamos que repose tapado en la nevera unos 30 minutos para que el ácido del limón haga su efecto y adquiera, además, ese toque de aroma a ajo."
                         "\n A la hora de cocinar el rape, retiramos los trozos de ajo y lo salpimentamos. Ponemos a calentar el aceite hasta que esté bien caliente pero sin que humee. Luego, en un recipiente, ponemos 2 de cucharadas de harina y en otro recipiente cascamos y batimos 1 huevo con una pizca de sal. El otro huevo lo reservamos por si se nos acaba el primero. Uno a uno, vamos enharinando y pasado por huevo los trozos de rape."
                         "\n Directamente, tras pasar los trozos de rape por el huevo, los metemos en la sartén. Iremos poniendo unos cuantos trozos sin sobrecargar la fritura para que no nos salgan aceitosos. Si se acaba el huevo o la harina, ponemos un poco más."
                         "\n Los freímos el rape rebozado durante unos minutos, el tiempo justo para que los trozos de rape cojan un bonito color dorado. No hace falta mucho más pues el pescado se hace rápido. Conforme se van haciendo, los retiramos."
                         "\n Una vez fritos, los dejamos reposar sobre papel absorbente para retirarles el exceso de aceite."
                         "\n Servimos los fritos de rape o fritos de pixín acompañados con medio limón, para que quien quiera que le ponga, un poco de lechuga, que le da un toque fresco, y mayonesa para mojar.",
                   id_usuario=3),

            Receta(nombre="Torrijas al horno",
                   descripcion="Las torrijas es uno de los postres más tradicionales de nuestro recetario. Se dice que, tiempo atrás, se preparaban para ayudar a las parturientas a reponer fuerzas y ya más adelante, se convirtieron en postre de Cuaresma y Semana Santa.",
                   imagen="https://imag.bonviveur.com/torrijas-al-horno-foto-principal.webp",
                   video="",
                   pasos="En un cazo profundo, vertemos 500 ml de leche entera, 1 rama de canela y la piel de medio limón. Llevamos el cazo al fuego y dejamos que la leche se caliente pero que no llegue a hervir. Se trata de infusionar la leche con la canela y la piel del limón así que, antes de que hierva retiraremos el cazo del fuego y lo reservaremos hasta que no esté muy caliente."
                         "\n Retiramos la canela y la piel de limón de la leche. Añadimos 50 g de azúcar y batimos bien para que el azúcar no se quede en el fondo del cazo."
                         "\n Disponemos 6 rebanadas de pan de molde gruesas en una fuente un poco profunda y vertemos sobre ellas la leche infusionada. Dejamos que se empapen bien las rebanadas de pan, pero teniendo cuidado de que no pase demasiado tiempo y el pan se rompa."
                         "\n Después de 5 minutos aproximadamente el pan habrá absorbido la leche."
                         "\n Batimos 2 huevos y pasamos cada rebanada de pan mojado en leche por el huevo."
                         "\n Precalentamos el horno a 200 ºC. Preparamos una bandeja con papel de horno y ponemos sobre este las rebanadas de pan mojadas leche y huevo. Llevamos la bandeja al horno con la función grill. Dejamos que las torrijas se cocinen por un lado durante 5 minutos. Les damos la vuelta y las hacemos por el otro lado otros 5 minutos."
                         "\n Mientras se cocinan las torrijas, preparamos una fuente con 50 g de azúcar y una cucharadita de canela en polvo para rebozar después las torrijas."
                         "\n Una vez hechas las torrijas, las sacamos del horno y las rebozamos con el azúcar y canela que habíamos preparado."
                         "\n Servimos las torrijas recién hechas aunque se conservan bastante bien hasta un par de días.",
                   id_usuario=4),

            Receta(nombre="Berberechos al vapor",
                   descripcion="Los berberechos son muy sabrosos y fáciles de preparar. Si tenemos la suerte de conseguir unos berberechos de las rías gallegas, grandes y bien llenitos, os aseguro que vais a sorprenderos con esta delicia de aperitivo. Son perfectos para darnos un homenaje en un día especial y aunque, como todo, se han encarecido bastante, todavía podemos seguir diciendo que son una opción de marisco económica.",
                   imagen="https://imag.bonviveur.com/como-hacer-berberechos-al-vapor-perfectos.webp",
                   video="",
                   pasos="Aunque hoy en día los berberechos vienen depurados, es conveniente ponerlos en agua salada un rato antes de prepararlos para que suelten las posibles arenas que puedan traer. Es realmente desagradable encontrarse con arenas al masticar un berberecho, así que para evitarlo, ponemos un poco de agua fría con sal en un bol, echamos los berberechos y, con cuidado para no romperlos, los movemos con las manos."
                         "\n Una vez limpios, los escurrimos, los pasamos a una cazuela y los acercamos al fuego para que se cocinen en su vapor. No ponemos agua en el fondo, ya que ellos van soltando el agua suficiente para la generación de vapor a medida que se van abriendo. Una cazuela con tapa de cristal resulta ideal para realizar este plato ya que así, podremos ver cuándo están abiertos sin necesidad de destaparla evitando así que se escape el vapor."
                         "\n Vamos observando cómo se van cocinando los berberechos que, después de unos 7-8 minutos, deberían estar abiertos. En ese momento los retiramos para que no se pasen de cocción. Estos tiempos son relativos, pues dependerá de factores como si el material de nuestra olla conduce mejor o peor el calor, de su tamaño, del espacio que tengan en el interior de la olla o de la intensidad y tipo de fuego. Por ello, lo mejor es observarlos y, sin perderlos de vista, retirarlos del fuego cuando veamos que están todos abiertos."
                         "\n Los servimos inmediatamente para degustarlos bien calentitos y al natural, para así disfrutar de todo su sabor.",
                   id_usuario=4),

            Receta(nombre="Salsa romesco",
                   descripcion="Cuando pruebas la salsa romesco por primera vez, sabes al instante que va a ser un sabor difícil de olvidar, que la vas a querer disfrutar más y más, y vas a entender por qué se trata de una de las preparaciones culinarias emblema de la gastronomía catalana.",
                   imagen="https://imag.bonviveur.com/salsa-romesco.webp",
                   video="",
                   pasos="Antes que nada, para empezar a preparar la salsa, vamos a poner a calentar el horno a 180 ºC. A continuación, cogemos 1 kg de tomates maduros, los lavamos y les quitamos el tallo. Los engrasamos con aceite y los disponemos en una bandeja o fuente apta para horno, junto con una cabeza de ajos pequeña. Horneamos durante 30 minutos."
                         "\n Mientras los tomates están en el horno, cogemos las ñoras y les vamos a hacer un corte. Las ponemos en un bol y las cubrimos con un poco de agua hirviendo. Por último, con una cuchara (para no quemarnos), las hundimos para que el agua entre por el corte que hicimos y no se queden flotando."
                         "\n Hecho esto, ponemos a calentar ahora un poco de aceite de oliva para freír y, cuando esté caliente pero sin que llegue a humear, freímos por ambos lados 1 rebanada de pan de aproximadamente 30 g. Dejamos reposar sobre papel absorbente."
                         "\n Luego, tenemos que tostar 50 g de almendras y unos 30 g de avellanas. Si las almendras tienen piel, ponemos un cazo con agua a calentar, hervimos las almendras 1 minuto, las sacamos y les retiramos la piel. Las avellanas, si tienen piel se la dejamos. Cuando saquemos los tomates y el ajo, bajamos el horno a 160 ºC y metemos los frutos secos unos minutos, hasta que cojan color. Al sacarlos del horno, quitamos la piel de las avellanas frotándolas todas juntas dentro de un paño."
                         "\n En el vaso de la batidora, ponemos los tomates sin el pedúnculo, los ajos pelados, la carne de la ñoras (que habremos raspado con una cuchara), la rebanada de pan frito rota en tres o 4 trozos, las almendras y las avellanas. Trituramos todo junto hasta obtener una crema de textura lisa. Si la batidora es poco potente, se pueden pelar los tomates para evitar los restos de pieles."
                         "\n Ya solo nos queda aliñar la salsa con unas 3 o 4 cucharadas de aceite de oliva virgen extra, 1 cucharada de vinagre (aunque se puede ajustar al gusto), sal y pimienta. Finalizamos con unos golpes más de batidora para que se integre bien."
                         "\n Podemos consumir enseguida, conservar varios días en la nevera o congelar.", id_usuario=4),

            Receta(nombre="Magdalenas de chocolate",
                   descripcion="Los ingredientes de estas magdalenas de chocolate nunca faltan en nuestra despensa, por lo que no tenemos excusa para no encender el horno y prepararlas. La mejor manera de degustar estas magdalenas es con un buen vaso de leche, y ya podremos disfrutar de un delicioso desayuno o merienda.",
                   imagen="https://imag.bonviveur.com/magdalenas-de-chocolate-en-el-plato.webp",
                   video="",
                   pasos="Precalentamos el horno a 185 ºC. Derretimos los 75 gramos de mantequilla y los 100 gramos de chocolate negro en un cazo, justo hasta que se derrita, que no se caliente en exceso."
                         "\n Pasamos la mezcla de mantequilla y chocolate a un bol. Agregamos los 85 gramos de azúcar moreno y mezclamos bien."
                         "\n A continuación, integramos los dos huevos medianos. Mezclamos hasta tener una masa homogénea."
                         "\n Tamizamos, sobre la mezcla anterior, los 180 gramos de harina, los 40 gramos de almendras molidas, los tres cuartos de cucharadita de levadura química y los tres cuartos de cucharadita de bicarbonato sódico."
                         "\n Mezclamos, poco a poco, con unas varillas mientras vamos añadiendo los 120 mililitros de leche entera."
                         "\n Cuando tengamos una masa homogénea, integramos los 100 gramos de chips de chocolate. Nos guardamos unos cuantos para poner al final sobre la masa."
                         "\n Repartimos la masa en las cápsulas y colocamos unos cuantos chips de chocolate sobre las magdalenas. Horneamos 20-25 minutos o hasta que pinchemos con un palillo y salga limpio. Dejamos reposar 5 minutos en el molde y luego pasamos a una rejilla hasta que se enfríen por completo.",
                   id_usuario=5),

            Receta(nombre="Lubina a la donostiarra",
                   descripcion="La lubina a la donostiarra es una receta muy rica destinada a triunfar. Ya solo escuchar «a la donostiarra» es empezar a sonar campanas de gloria en la cabeza.",
                   imagen="https://imag.bonviveur.com/presentacion-principal-de-la-lubina-a-la-donostiarra.webp",
                   video="",
                   pasos="Para hacer una buena lubina a la donostiarra hay que elegir un buen producto, a ser posible fresco. En la pescadería hay que pedir que lo evisceren y que lo limpien. Además, interesa que nos abran la lubina en libro."
                         "\n Comenzamos la receta precalentando el horno a 180 ºC con calor arriba y abajo, y aire si disponemos de él. Se pelan, se limpian y se cortan las patatas en panadera, es decir, en rodajas de medio centímetro de grosor. Se pone en una fuente de horno una cucharada de aceite de oliva y se hace una cama con las patatas cortadas en rodajas. Como la cocción de la patata es de más tiempo que la de la lubina, hay que cocinar las patatas antes para que se vayan haciendo. Se dejan en el horno unos 15-20 minutos si tenemos aire (ya que el aire acelera el proceso de cocción) si no, habrá que dejarlas sobre 30 minutos. Se les puede poner un poco de agua, sin cubrirlas, para que no se resequen demasiado."
                         "\n Una vez ha transcurrido el tiempo de cocción de las patatas en el horno, pinchamos una y si entra bien el cuchillo, sacamos la fuente del horno. Se coloca la lubina abierta en libro con la piel hacia abajo, sobre la cama de patatas panadera. Se pone una pizca de sal a la lubina, se apaga el aire del horno y se vuelve a meter la fuente unos 15 minutos para que el pescado quede en su punto. El tiempo de cocción de la lubina depende del tamaño de esta. Se toma como referencia una lubina de acuicultura de unos 600 g con cabeza."
                         "\n Mientras la lubina está en el horno, cuando queden 5 minutos para sacar la fuente, se pone una sartén al fuego con los 4 dientes de ajo laminados, las guindillas cayena (una o dos al gusto) y los 30 ml de aceite de oliva virgen extra. Se ponen a fuego medio para que se doren poco a poco. Cuando estén dorados, se aparta la sartén del fuego y se añaden los 10 ml de vinagre de vino blanco, con cuidado de que no salte."
                         "\n Se saca la fuente del horno, se riega la lubina con el refrito de ajos y se espolvorea con un poco de perejil fresco picado. El perejil se puede añadir a la sartén y freírlo en el último momento cuando retiramos la sartén del fuego o, como hemos hecho, se pude incorporar, sin freírlo, a la fuente con el pescado recién sacado del horno."
                         "\n Se sirve la lubina acompañada de unas patatas panadera. Se puede acompañar de un buen vino blanco, un cava o un champagne.",
                   id_usuario=5),

            Receta(nombre="Espaguetis carbonara",
                   descripcion="Los espaguetis a la carbonara es probablemente la forma más internacional de preparar esta pasta. La auténtica salsa carbonara de italia contiene yema de huevo, queso y bacon. No tiene nata, ingrediente que le solemos añadir en España. Incluso hay muchas versiones que tan solo contienen nata. Puedes hacerla así, si quieres pero aquí, haremos unos espaguetis a la carbonara auténticos.",
                   imagen="https://images.pexels.com/photos/2703468/pexels-photo-2703468.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
                   video="",
                   pasos="Ponemos un puñadito de sal (generoso) en abundante agua hirviendo. Después añadimos los espagueti y los dejamos cocer aquí alrededor de 10 minutos. hasta que estén al «dente». Conviene removerlos con frecuencia sobre todo al principio de la cocción, para que no se peguen."
                         "\n Mientras se cuecen preparamos la carbonara. En un bol añadimos las yemas de los huevos. La clara es mejor guardarla para otra elaboración ya que, si la añadimos, parecerá más una tortilla de espaguetis, que una salsa en sí. Pero si no te importa, puedes añadirla. Añadimos también el queso rallado y mezclamos ambos ingredientes con un tenedor. Quedará una especie de masa muy densa y ésta, será la carbonara."
                         "\n En una sartén ponemos un pequeño chorrito de aceite. Cuando esté bien caliente, añadimos el bacon o la panceta, cortado en dados más bien pequeños. Pasados un par de minutos, cuando estén fritos, retiramos del fuego y reservamos"
                         "\n Una vez hecho esto y cuando los espaguetis estén cocinados, guardamos unos cuantos cucharones del caldo de la cocción. Después escurrimos los espaguetis del resto del caldo"
                         "\n Sin demora, ya que será el propio calor residual de los espagueti los que vayan a cocinar la carbonara, echamos la pasta en el bol donde la habíamos preparado. Añadimos el bacon, con el juguito que hayan podido soltar y un poco del caldo de la cocción. Removemos todo bien con un tenedor para que los espaguetis absorban toda la salsa. Si ves que queda muy densa, puedes añadir más caldo de la cocción, hasta que haya quedado una salsa muy cremosa (no olvides remover enérgicamente todo. La pasta es muy porosa y absorbe las salsa con relativa facilidad. Pero necesita ser removido para ayudar a este proceso)"
                         "\n Finalmente, cuando hayamos conseguido la cremosidad de la salsa deseado, espolvorear con abundante pimienta negra recién molida. Se dice que el nombre «carbonara» viene del color que le da esta especia, que recuerda el color del carbón. Servir inmediatamente",
                   id_usuario=5),
        ]

        ingredientesRecetas = [
            IngredienteReceta(receta_id=1, ingrediente_id=1, cantidad="150gr"),
            IngredienteReceta(receta_id=1, ingrediente_id=2, cantidad="80gr"),
            IngredienteReceta(receta_id=1, ingrediente_id=3, cantidad="3"),
            IngredienteReceta(receta_id=1, ingrediente_id=4, cantidad="200mm"),
            IngredienteReceta(receta_id=1, ingrediente_id=5, cantidad="2"),
            IngredienteReceta(receta_id=1, ingrediente_id=6, cantidad="6"),
            IngredienteReceta(receta_id=1, ingrediente_id=7, cantidad="125gr"),
            IngredienteReceta(receta_id=1, ingrediente_id=8, cantidad="2"),
            IngredienteReceta(receta_id=2, ingrediente_id=9, cantidad="200gr"),
            IngredienteReceta(receta_id=2, ingrediente_id=10, cantidad="1l"),
            IngredienteReceta(receta_id=2, ingrediente_id=7, cantidad="100gr"),
            IngredienteReceta(receta_id=2, ingrediente_id=11, cantidad="2 ramas"),
            IngredienteReceta(receta_id=2, ingrediente_id=12, cantidad="1"),
            IngredienteReceta(receta_id=3, ingrediente_id=13, cantidad="2"),
            IngredienteReceta(receta_id=3, ingrediente_id=10, cantidad="30g"),
            IngredienteReceta(receta_id=3, ingrediente_id=14, cantidad="1"),
            IngredienteReceta(receta_id=3, ingrediente_id=15, cantidad="1Kg"),
            IngredienteReceta(receta_id=3, ingrediente_id=16, cantidad="5gr"),
            IngredienteReceta(receta_id=3, ingrediente_id=17, cantidad="5gr"),
            IngredienteReceta(receta_id=3, ingrediente_id=18, cantidad="30gr"),
            IngredienteReceta(receta_id=3, ingrediente_id=19, cantidad="15gr"),
            IngredienteReceta(receta_id=3, ingrediente_id=20, cantidad=""),
            IngredienteReceta(receta_id=3, ingrediente_id=21, cantidad=""),
            IngredienteReceta(receta_id=3, ingrediente_id=22, cantidad=""),
            IngredienteReceta(receta_id=4, ingrediente_id=14, cantidad="1"),
            IngredienteReceta(receta_id=4, ingrediente_id=22, cantidad=""),
            IngredienteReceta(receta_id=4, ingrediente_id=20, cantidad="5gr"),
            IngredienteReceta(receta_id=5, ingrediente_id=23, cantidad="1kg"),
            IngredienteReceta(receta_id=5, ingrediente_id=24, cantidad="1 cucharadita"),
            IngredienteReceta(receta_id=5, ingrediente_id=8, cantidad="2 1/2"),
            IngredienteReceta(receta_id=5, ingrediente_id=22, cantidad="2 cucharadas"),
            IngredienteReceta(receta_id=5, ingrediente_id=25, cantidad="30g"),
            IngredienteReceta(receta_id=6, ingrediente_id=26, cantidad="700gr"),
            IngredienteReceta(receta_id=6, ingrediente_id=27, cantidad="300gr"),
            IngredienteReceta(receta_id=6, ingrediente_id=28, cantidad="1"),
            IngredienteReceta(receta_id=6, ingrediente_id=29, cantidad="1"),
            IngredienteReceta(receta_id=6, ingrediente_id=30, cantidad="1"),
            IngredienteReceta(receta_id=6, ingrediente_id=31, cantidad="1"),
            IngredienteReceta(receta_id=6, ingrediente_id=32, cantidad="1"),
            IngredienteReceta(receta_id=6, ingrediente_id=22, cantidad="70ml"),
            IngredienteReceta(receta_id=6, ingrediente_id=33, cantidad="30ml"),
            IngredienteReceta(receta_id=6, ingrediente_id=20, cantidad="1/2 cucharadita"),
            IngredienteReceta(receta_id=7, ingrediente_id=34, cantidad="2"),
            IngredienteReceta(receta_id=7, ingrediente_id=35, cantidad="1"),
            IngredienteReceta(receta_id=7, ingrediente_id=14, cantidad="1"),
            IngredienteReceta(receta_id=7, ingrediente_id=36, cantidad="50gr"),
            IngredienteReceta(receta_id=7, ingrediente_id=37, cantidad="75gr"),
            IngredienteReceta(receta_id=7, ingrediente_id=38, cantidad="150gr"),
            IngredienteReceta(receta_id=7, ingrediente_id=39, cantidad="400gr"),
            IngredienteReceta(receta_id=8, ingrediente_id=14, cantidad="1"),
            IngredienteReceta(receta_id=8, ingrediente_id=22, cantidad="1/2 Vaso"),
            IngredienteReceta(receta_id=8, ingrediente_id=31, cantidad="1-2"),
            IngredienteReceta(receta_id=8, ingrediente_id=20, cantidad="1 Pizca"),
            IngredienteReceta(receta_id=8, ingrediente_id=40, cantidad="1/2"),
            IngredienteReceta(receta_id=9, ingrediente_id=41, cantidad="400gr"),
            IngredienteReceta(receta_id=9, ingrediente_id=31, cantidad="1"),
            IngredienteReceta(receta_id=9, ingrediente_id=40, cantidad="1 chorrito"),
            IngredienteReceta(receta_id=9, ingrediente_id=20, cantidad="Al gusto"),
            IngredienteReceta(receta_id=9, ingrediente_id=21, cantidad="Al gusto"),
            IngredienteReceta(receta_id=9, ingrediente_id=43, cantidad=""),
            IngredienteReceta(receta_id=9, ingrediente_id=42, cantidad="2 cucharadas"),
            IngredienteReceta(receta_id=9, ingrediente_id=14, cantidad="1 o 2"),
            IngredienteReceta(receta_id=10, ingrediente_id=10, cantidad="500ml"),
            IngredienteReceta(receta_id=10, ingrediente_id=11, cantidad="1 rama"),
            IngredienteReceta(receta_id=10, ingrediente_id=12, cantidad="1/2"),
            IngredienteReceta(receta_id=10, ingrediente_id=7, cantidad="100gr"),
            IngredienteReceta(receta_id=10, ingrediente_id=13, cantidad="6"),
            IngredienteReceta(receta_id=10, ingrediente_id=14, cantidad="2"),
            IngredienteReceta(receta_id=10, ingrediente_id=44, cantidad="1 cucharadita"),
            IngredienteReceta(receta_id=11, ingrediente_id=46, cantidad=""),
            IngredienteReceta(receta_id=11, ingrediente_id=45, cantidad="1kg"),
            IngredienteReceta(receta_id=12, ingrediente_id=47, cantidad="1kg"),
            IngredienteReceta(receta_id=12, ingrediente_id=52, cantidad="1"),
            IngredienteReceta(receta_id=12, ingrediente_id=48, cantidad="1"),
            IngredienteReceta(receta_id=12, ingrediente_id=49, cantidad="1"),
            IngredienteReceta(receta_id=12, ingrediente_id=22, cantidad=""),
            IngredienteReceta(receta_id=12, ingrediente_id=50, cantidad="50gr"),
            IngredienteReceta(receta_id=12, ingrediente_id=51, cantidad="30gr"),
            IngredienteReceta(receta_id=12, ingrediente_id=33, cantidad="1 cucharada"),
            IngredienteReceta(receta_id=12, ingrediente_id=20, cantidad="Al gusto"),
            IngredienteReceta(receta_id=12, ingrediente_id=21, cantidad="Al gusto"),
            IngredienteReceta(receta_id=13, ingrediente_id=53, cantidad="75gr"),
            IngredienteReceta(receta_id=13, ingrediente_id=54, cantidad="100gr"),
            IngredienteReceta(receta_id=13, ingrediente_id=55, cantidad="85gr"),
            IngredienteReceta(receta_id=13, ingrediente_id=14, cantidad="2"),
            IngredienteReceta(receta_id=13, ingrediente_id=56, cantidad="180gr"),
            IngredienteReceta(receta_id=13, ingrediente_id=57, cantidad="40gr"),
            IngredienteReceta(receta_id=13, ingrediente_id=58, cantidad="3/4 cucharadita"),
            IngredienteReceta(receta_id=13, ingrediente_id=59, cantidad="3/4 cucharadita"),
            IngredienteReceta(receta_id=13, ingrediente_id=60, cantidad="120ml"),
            IngredienteReceta(receta_id=13, ingrediente_id=61, cantidad="100gr"),
            IngredienteReceta(receta_id=14, ingrediente_id=62, cantidad="2"),
            IngredienteReceta(receta_id=14, ingrediente_id=22, cantidad="30ml"),
            IngredienteReceta(receta_id=14, ingrediente_id=63, cantidad="1 o 2"),
            IngredienteReceta(receta_id=14, ingrediente_id=31, cantidad="4"),
            IngredienteReceta(receta_id=14, ingrediente_id=64, cantidad="1 0 2"),
            IngredienteReceta(receta_id=14, ingrediente_id=33, cantidad="10ml"),
            IngredienteReceta(receta_id=14, ingrediente_id=65, cantidad="Al gusto"),
            IngredienteReceta(receta_id=14, ingrediente_id=20, cantidad="Al gusto"),
            IngredienteReceta(receta_id=15, ingrediente_id=66, cantidad="400gr"),
            IngredienteReceta(receta_id=15, ingrediente_id=14, cantidad="2"),
            IngredienteReceta(receta_id=15, ingrediente_id=67, cantidad="150gr"),
            IngredienteReceta(receta_id=15, ingrediente_id=68, cantidad="120gr"),
            IngredienteReceta(receta_id=15, ingrediente_id=20, cantidad="Al gusto"),
            IngredienteReceta(receta_id=15, ingrediente_id=21, cantidad="Al gusto"),
            IngredienteReceta(receta_id=15, ingrediente_id=22, cantidad="1 chorrito"),
        ]

        comentarios = [
            Comentario(usuario_id=1, receta_id=1,
                       contenido="Se me olvidó mencionar que si quereis más recetas dadle a me gusta!"),

            Comentario(usuario_id=3, receta_id=1, padre_id=1,
                       contenido="Hecho!!"),

            Comentario(usuario_id=2, receta_id=1,
                       imagen="https://images.pexels.com/photos/8942530/pexels-photo-8942530.jpeg?auto=compress&cs"
                              "=tinysrgb&w=1260&h=750&dpr=1",
                       contenido="Buenísima receta!"),

            Comentario(usuario_id=3, receta_id=1, padre_id=3,
                       imagen="http://localhost:5000/static/comentarios/tartaQueso.jpg",
                       contenido="Te ha quedado genial! Aquí mi resultado"),

            Comentario(usuario_id=5, receta_id=2,
                       imagen="https://st.depositphotos.com/2461721/2717/i/450/depositphotos_27175187-stock-photo"
                              "-rice-pudding-top-view.jpg",
                       contenido="Aqui mi resultado!"),

            Comentario(usuario_id=4, receta_id=2,
                       imagen="https://st.depositphotos.com/2461721/2717/i/450/depositphotos_27175187-stock-photo"
                              "-rice-pudding-top-view.jpg",
                       contenido=""),

            Comentario(usuario_id=2, receta_id=5,
                       contenido="Tremenda pizza! Quiero ver los resultados de los demás"),

            Comentario(usuario_id=1, receta_id=5, padre_id=7,
                       imagen="https://images.pexels.com/photos/708587/pexels-photo-708587.jpeg?auto=compress&cs"
                              "=tinysrgb&w=1260&h=750&dpr=1",
                       contenido=""),

            Comentario(usuario_id=1, receta_id=8,
                       imagen="https://st2.depositphotos.com/1364913/7108/i/450/depositphotos_71089381-stock-photo"
                              "-garlic-dip-top-view.jpg",
                       contenido="Me encanta la Alioli! Buena receta"),

            Comentario(usuario_id=3, receta_id=10,
                       contenido="Receta muy sencilla, la recomiendo"),

            Comentario(usuario_id=5, receta_id=10,
                       imagen="https://imag.bonviveur.com/torrijas-al-horno-foto-principal.webp",
                       contenido="Me encantó la receta!"),

            Comentario(usuario_id=1, receta_id=12,
                       imagen="https://imag.bonviveur.com/salsa-romesco.webp",
                       contenido="Nunca la probé antes, pero está buenísima! La recomienndo"),

            Comentario(usuario_id=2, receta_id=14,
                       contenido="No soy de comer pescado, pero este está buenísimo!"),

            Comentario(usuario_id=3, receta_id=14, padre_id=13,
                       imagen="https://imag.bonviveur.com/presentacion-principal-de-la-lubina-a-la-donostiarra.webp",
                       contenido="Yo igual! Aqui mi resultado"),

            Comentario(usuario_id=4, receta_id=15,
                       imagen="https://images.pexels.com/photos/2703468/pexels-photo-2703468.jpeg?auto=compress&cs"
                              "=tinysrgb&w=1260&h=750&dpr=1",
                       contenido="Me flipa la salsa carbonara!"),

            Comentario(usuario_id=2, receta_id=15, padre_id=15,
                       contenido="Te quedó increible!")
        ]

        likes = [
            Like(usuario_id=1, receta_id=1),
            Like(usuario_id=1, receta_id=2),
            Like(usuario_id=1, receta_id=3),
            Like(usuario_id=1, receta_id=6),
            Like(usuario_id=1, receta_id=8),
            Like(usuario_id=1, receta_id=10),
            Like(usuario_id=1, receta_id=12),
            Like(usuario_id=2, receta_id=4),
            Like(usuario_id=2, receta_id=5),
            Like(usuario_id=2, receta_id=6),
            Like(usuario_id=2, receta_id=2),
            Like(usuario_id=2, receta_id=1),
            Like(usuario_id=2, receta_id=5),
            Like(usuario_id=2, receta_id=8),
            Like(usuario_id=3, receta_id=7),
            Like(usuario_id=3, receta_id=8),
            Like(usuario_id=3, receta_id=9),
            Like(usuario_id=3, receta_id=4),
            Like(usuario_id=3, receta_id=14),
            Like(usuario_id=3, receta_id=3),
            Like(usuario_id=3, receta_id=1),
            Like(usuario_id=4, receta_id=10),
            Like(usuario_id=4, receta_id=11),
            Like(usuario_id=4, receta_id=12),
            Like(usuario_id=4, receta_id=3),
            Like(usuario_id=4, receta_id=8),
            Like(usuario_id=4, receta_id=9),
            Like(usuario_id=4, receta_id=1),
            Like(usuario_id=5, receta_id=13),
            Like(usuario_id=5, receta_id=14),
            Like(usuario_id=5, receta_id=15),
            Like(usuario_id=5, receta_id=5),
            Like(usuario_id=5, receta_id=7),
            Like(usuario_id=5, receta_id=12),
            Like(usuario_id=5, receta_id=10),
            Like(usuario_id=5, receta_id=1),

        ]

        # add data from lists
        for usuario in usuarios:
            db.session.add(usuario)
        for ingrediente in ingredientes:
            db.session.add(ingrediente)
        for receta in tuple(recetas):
            db.session.add(receta)
        for comentario in comentarios:
            db.session.add(comentario)
        for like in likes:
            db.session.add(like)
        for ingredienteReceta in ingredientesRecetas:
            db.session.add(ingredienteReceta)
        # commit changes in database
        db.session.commit()


class Usuario(db.Model):
    """
    User entity

    Store user data
    """
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80), unique=True, nullable=False)
    nick = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    imagen = db.Column(db.String(150), unique=False, nullable=False)

    hashed_password = db.Column(db.Text)

    is_admin = db.Column(db.Boolean, default=False, server_default="false")
    is_active = db.Column(db.Boolean, default=True, server_default="true")

    @property
    def identity(self):
        """
        *Required Attribute or Property*

        flask-praetorian requires that the user class has an ``identity`` instance
        attribute or property that provides the unique id of the user instance
        """
        return self.id

    @property
    def rolenames(self):
        """
        *Required Attribute or Property*

        flask-praetorian requires that the user class has a ``rolenames`` instance
        attribute or property that provides a list of strings that describe the roles
        attached to the user instance
        """
        return "admin" if self.is_admin else "user"

    @property
    def password(self):
        """
        *Required Attribute or Property*

        flask-praetorian requires that the user class has a ``password`` instance
        attribute or propelikes = db.Table('like',
                 db.Column('receta_id', db.Integer, db.ForeignKey('receta.id'), primary_key=True),
                 db.Column('usuario_id', db.Integer, db.ForeignKey('usuario.id'), primary_key=True)
                 )rty that provides the hashed password assigned to the user
        instance
        """

        return self.hashed_password

    @classmethod
    def lookup(cls, nombre):
        """
        *Required Method*

        flask-praetorian requires that the user class implements a ``lookup()``
        class method that takes a single ``username`` argument and returns a user
        instance if there is one that matches or ``None`` if there is not.
        """
        return cls.query.filter_by(nombre=nombre).one_or_none()

    @classmethod
    def identify(cls, id_user):
        """
        *Required Method*

        flask-praetorian requires that the user class implements an ``identify()``
        class method that takes a single ``id`` argument and returns user instance if
        there is one that matches or ``None`` if there is not.
        """
        return cls.query.get(id_user)

    def is_valid(self):
        return self.is_active

    # specify string for repr
    def __repr__(self):
        return f"<Usuario {self.nombre}>"


class IngredienteReceta(db.Model):
    __tablename__ = 'ingrediente_receta'
    receta_id = db.Column(ForeignKey('receta.id'), primary_key=True)
    ingrediente_id = db.Column(ForeignKey('ingrediente.id'), primary_key=True)
    cantidad = db.Column(db.String(200), unique=False, nullable=False)

    ingrediente = relationship("Ingrediente", back_populates="recetas")
    receta = relationship("Receta", back_populates="ingredientes")


class Receta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80), unique=True, nullable=False)
    descripcion = db.Column(db.String(200), unique=False, nullable=False)
    imagen = db.Column(db.String(150), unique=False, nullable=False)
    video = db.Column(db.String(200), unique=False, nullable=True)
    pasos = db.Column(db.String(300), unique=False, nullable=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=True)

    usuario = relationship("Usuario", backref="recetas")

    ingredientes = relationship("IngredienteReceta", back_populates="receta", cascade="all, delete")

    is_active = db.Column(db.Boolean, default=True, server_default="true")

    def __repr__(self):
        return f"<Receta {self.nombre}>"


class Ingrediente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80), unique=False, nullable=False)

    recetas = relationship("IngredienteReceta", back_populates="ingrediente", cascade="all, delete")

    def __repr__(self):
        return f"<Ingrediente {self.nombre}>"


class Like(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'))
    receta_id = db.Column(db.Integer, db.ForeignKey('receta.id'))

    receta = relationship("Receta", backref="likes")
    usuario = relationship("Usuario", backref="likes")


class Comentario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'))
    receta_id = db.Column(db.Integer, db.ForeignKey('receta.id'))
    padre_id = db.Column(db.Integer, db.ForeignKey('comentario.id'), nullable=True)
    imagen = db.Column(db.String(150), unique=False, nullable=True)
    contenido = db.Column(db.String(250), unique=False, nullable=False)

    receta = relationship("Receta", backref="comentarios")
    usuario = relationship("Usuario", backref="comentarios")
    padre = relationship("Comentario", remote_side=[id])


class UsuarioSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Usuario
        include_relationships = True
        load_instance = True
        sqla_session = db.session


class RecetaSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Receta
        include_relationships = True
        load_instance = True
        sqla_session = db.session


class IngredienteSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Ingrediente
        include_relationships = True
        load_instance = True
        sqla_session = db.session


class LikeSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Like
        include_relationships = True
        load_instance = True
        sqla_session = db.session


class ComentarioSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Comentario
        include_relationships = True
        load_instance = True
        sqla_session = db.session
