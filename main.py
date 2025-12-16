import time
import sys

def countdown(t: int):
    """
    Counts down from t seconds and displays the time, 
    updating the display on the same line.
    """
    print("Iniciando contagem regressiva...")
    while t >= 0:
        mins, secs = divmod(t, 60)
        # Formats the time as MM:SS
        timer = f'{mins:02d}:{secs:02d}' 
        
        # \r (Carriage Return) moves the cursor to the beginning of the line
        print(timer, end="\r") 
        sys.stdout.flush() # Ensures the timer updates immediately

        time.sleep(1)
        t -= 1

    # After the loop finishes (t is -1), print the final message and clear the line
    print('Tá na hora!             ') 

# --- Main Program Execution ---
if __name__ == "__main__":
    while True: # Loop to allow multiple countdowns
        try:
            t_input = input("Digite o tempo para a contagem regressiva em segundos (ou 'sair' para encerrar): ")

            if t_input.lower() == 'sair':
                print("Contagem regressiva encerrada.")
                break
            
            # Convert input to integer and start the countdown
            seconds = int(t_input)
            if seconds < 0:
                print("O tempo deve ser um número positivo.")
                continue

            countdown(seconds) 

        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")
        except KeyboardInterrupt:
            print("\nContagem regressiva interrompida.")
            break
    