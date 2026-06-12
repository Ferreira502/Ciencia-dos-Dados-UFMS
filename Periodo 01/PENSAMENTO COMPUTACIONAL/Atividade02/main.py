
from time import sleep, time
from ev3dev2.motor import MoveTank, OUTPUT_A, OUTPUT_B, SpeedPercent
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_5
from ev3dev2.sensor.lego import ColorSensor, UltrasonicSensor

# Configuracao esperada do robo:
# in1 = sensor de cor esquerdo
# in2 = sensor ultrassonico
# in5 = sensor de cor direito
# outA = motor esquerdo
# outB = motor direito

tank = MoveTank(OUTPUT_A, OUTPUT_B)
color_left = ColorSensor(INPUT_1)
ultra_front = UltrasonicSensor(INPUT_2)
color_right = ColorSensor(INPUT_5)

VEL_RETA = 18
VEL_CURVA = 6
VEL_RETA_LENTA = 10
DISTANCIA_OBSTACULO = 14
DISTANCIA_LIVRE = 20
TEMPO_GIRO_90 = 0.75
TEMPO_DESVIO_LATERAL = 0.90
TEMPO_AVANCO_EXTRA = 0.60


def mover(esquerda, direita):
    tank.on(SpeedPercent(esquerda), SpeedPercent(direita))


def parar():
    tank.off(brake=True)


def cor_esquerda():
    return color_left.color_name


def cor_direita():
    return color_right.color_name


def obstaculo_a_frente():
    distancia = ultra_front.distance_centimeters
    return distancia != 255 and distancia <= DISTANCIA_OBSTACULO


def seguir_linha():
    esquerda = cor_esquerda()
    direita = cor_direita()

    if esquerda == 'White' and direita == 'White':
        mover(VEL_RETA, VEL_RETA)
    elif esquerda == 'Black' and direita == 'White':
        mover(VEL_CURVA, VEL_RETA)
    elif esquerda == 'White' and direita == 'Black':
        mover(VEL_RETA, VEL_CURVA)
    else:
        mover(VEL_RETA_LENTA, VEL_RETA_LENTA)


def virar_direita():
    mover(16, -16)
    sleep(TEMPO_GIRO_90)
    parar()


def virar_esquerda():
    mover(-16, 16)
    sleep(TEMPO_GIRO_90)
    parar()


def avancar_tempo(velocidade, segundos):
    mover(velocidade, velocidade)
    sleep(segundos)
    parar()


def procurar_linha(tempo_limite=3.0):
    inicio = time()

    while time() - inicio < tempo_limite:
        if cor_esquerda() == 'Black' or cor_direita() == 'Black':
            return True

        mover(8, 12)
        sleep(0.03)

    return False


def desviar_obstaculo():
    parar()
    sleep(0.2)

    # Sai para a direita da linha
    avancar_tempo(-10, 0.20)
    virar_direita()
    avancar_tempo(16, TEMPO_DESVIO_LATERAL)
    virar_esquerda()

    # Passa ao lado do cubo
    inicio = time()
    while time() - inicio < 2.5:
        if ultra_front.distance_centimeters == 255 or ultra_front.distance_centimeters >= DISTANCIA_LIVRE:
            break

        mover(14, 14)
        sleep(0.03)

    parar()
    avancar_tempo(14, TEMPO_AVANCO_EXTRA)

    # Volta para a linha
    virar_esquerda()
    encontrou = procurar_linha()
    parar()

    if encontrou:
        virar_direita()
    else:
        # Fallback: volta para a orientacao original mesmo se nao enxergar a linha de imediato
        virar_direita()
        avancar_tempo(10, 0.40)


while True:
    if obstaculo_a_frente():
        desviar_obstaculo()
    else:
        seguir_linha()

    sleep(0.01)
