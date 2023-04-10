from gameData import data
import random


def randomAccount():
    """Retireve random account data"""
    account = random.randint(1, 49)
    return data[account]


def compareAccounts(account, account2):
    """Compare two retreived accounts from data"""
    print(
        f"{account['name']}, a {account['description']} , from {account['country']}")
    print(
        f"{account2['name']}, a {account2['description']} , from {account2['country']}")

    # compare the follower account from the retrieved account data and return the correct one
    if account["follower_count"] > account2["follower_count"]:
        # print("A")
        return account
    else:
        # print("B")
        return account2


def userChoice(account, account2):
    """Check if the user answerd correctly based on the two account displayed"""
    continue_game = True
    while continue_game:
        # store the correct account in a variable 'result'
        result = compareAccounts(account, account2)
        if result == account2:
            answer = "B"
        else:
            answer = "A"

        choice = input(
            "Which account has a higher following?. \n 'A' or 'B'").upper()

        if choice == answer:
            # add to score counter
            global score_counter
            score_counter += 1

            print(score_counter)
            print("Correct")
            # keep the correct answer and compare it with a random one
            account2 = randomAccount()
            userChoice(account=result, account2=account2)

            return True
        else:
            # exit the game when answered incorrectly
            print(f"That was incorrect \n Final score was {score_counter} ")
            continue_game = False
            return False


score_counter = int()
account = randomAccount()
account2 = randomAccount()
# run the coder
verdict = userChoice(account=account, account2=account2)
