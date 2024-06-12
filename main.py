import test_Markov

def main():
    model = test_Markov.makeWordModel("MDR_Text.txt")
    word_chain = test_Markov.generateWordChain(model, 60)
    print("This is your word chain:", word_chain)

main()