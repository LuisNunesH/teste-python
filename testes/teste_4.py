import asyncio
import time

async def rede(tempo):
    print(f"Chamada de rede de {tempo} segundo(s)")
    await asyncio.sleep(tempo)
    print(f"Chamada de rede de {tempo} segundo(s) concluída")
    return tempo

async def main():
    inicio = time.time()

    await asyncio.gather(
        rede(2),
        rede(7),
        rede(3)
    )

    tempo_total = time.time() - inicio
    print(f"Tempo total de execução: {tempo_total:.2f} segundo(s)")

if __name__ == '__main__':
    asyncio.run(main())