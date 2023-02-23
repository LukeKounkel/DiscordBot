import discord
from discord.ext import commands 
from keep_alive import keep_alive
import random

client = commands.Bot(command_prefix = "$")

#informs me when the program is running sucessfully
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

#loans money between people
@client.command()
async def loan(ctx, loanval, loanee):
  username = str(ctx.message.author)
  username = username[-4:]
  loan_value = int(loanval)
  loanee_username = str(loanee)

  f = open(f"{username}.txt")
  contents = int(f.read())
  f.close()

  point_total = int(contents)

  if loan_value > point_total:
    await ctx.send("No accruing massive amounts of debt on my watch")

  elif loan_value < 0:
    await ctx.send("no stealing bubby")

  elif loan_value >= 0:
    f = open(f"{username}.txt")
    contents = int(f.read())
    f.close()

    loaner_total = int(contents) - loan_value

    f = open(f"{username}.txt", "w")
    f.write(str(loaner_total))
    f.close()

    f = open(f"{loanee_username}.txt")
    contents = int(f.read())
    f.close()

    loanee_total = int(contents) + loan_value
    f = open(f"{loanee_username}.txt", "w")
    f.write(str(loanee_total))
    f.close()

    await ctx.send(f"The transaction is complete. You now have {loaner_total}, and {loanee_username} now has {loanee_total}")


#gives a random number between 1 and 1000
@client.command(aliases = ['randomnumber', 'griffinisapoopyhead'])
async def rand(ctx):
  await ctx.send(f"your'e random number is {random.randint(1, 1000)}")


#just a greeting to god
@client.command()
async def hello(ctx):
  response = random.randchoice(["I am god (:"])
  await ctx.send(response)

#A way to gamble for small amounts 
@client.command()
async def gamble(ctx):
  username = str(ctx.message.author)
  username = username[-4:]

  f = open(f"{username}.txt")
  contents = int(f.read())
  f.close()

  if contents <= 25:
    await ctx.send("you need 25 points to gamble on this")

  
  else:  
    gamble_int = random.randint(-25, 25)
    f = open(f"{username}.txt")
    contents = int(f.read())
    f.close()

    point_total = int(contents) + gamble_int
    f = open(f"{username}.txt", "w")
    f.write(str(point_total))
    f.close()

    await ctx.send(f"I just changed your point value by {gamble_int}, and it is now {point_total}")


#a way to ask god why he did something
@client.command()
async def why_god(ctx):
  username = str(ctx.message.author)
  username = username[-4:]

  reasons = ["Trust Me. I have My reasons.", "So you will grow.", "You never prayed.", "So you’ll rely on Me.", "Just Wait.", "I have something better in mind.", "I’m protecting you.", "I’m making you more like Jesus.", "Because I love you.", "Fuck you dumbass", "My ways are mysterious to those that aren't enlightened", "GriffBot (my archrival) would have wanted it, so I had to prevent it.", "I'm going hit you with a bus.", "Your suffering is the only true way to make me happy.", "Hippity-Hoppity, I like giving children leukemia"]

  chosen_reason = random.choice(reasons)

  if username == "1991":
    await ctx.send("You don't deserve an answer to that question Spencer. All people of the earth are my children, but you are the one exeption.")

  else:
    await ctx.send(f"{chosen_reason}")


#a way to potentially gamble for very large amounts
@client.command()
async def wager(ctx, arg):
  username = str(ctx.message.author)
  username = username[-4:]

  wager_value1 = int(arg)

  f = open(f"{username}.txt")
  contents = int(f.read())
  f.close()

  point_total = int(contents)

  if wager_value1 > point_total: 
    await ctx.send("you don't have enough points to wager")

  else: 
    wager_value2 = wager_value1 * (random.randint(-1, 1))
    #the whole wager value 1/2 thing is just so multiplication by 0 does't make this while loop infinite

    while wager_value2 == 0:
      wager_value2 = wager_value1 * (random.randint(-1, 1))
    point_total = int(contents) + wager_value2

    f = open(f"{username}.txt", "w")
    f.write(str(point_total))
    f.close()

    await ctx.send(f"I just changed your point value by {wager_value2}, and it is now {point_total}")


#this shows the user what their current account balance is
@client.command()
async def bal(ctx):
  username = str(ctx.message.author)
  username = username[-4:]

  f = open(f"{username}.txt")
  contents = int(f.read())
  f.close() 

  await ctx.send(f"Your current balance is {contents}")


#starts a game of higher or lower where players try to guess towards a number with only higher/lower as hints
@client.command()
async def high_low(ctx):
  guess_count = 1
  f = open("guess_count.txt", "w")   
  f.write(str(guess_count))
  f.close()

  hlusername = str(ctx.message.author)
  hlusername = hlusername[-4:]
  f = open("high_low username.txt", "w")   
  f.write(str(hlusername))
  f.close()

  goal_number = random.randint(1, 100)
  f = open("goal_number.txt", "w")   
  f.write(str(goal_number))
  f.close()

  f = open(f"{hlusername}.txt")
  contents = int(float(f.read()))
  f.close() 

  point_total = int(contents) -50
  f = open(f"{hlusername}.txt", "w")
  f.write(str(point_total))
  f.close()

  await ctx.send("You've started an HL game. Now send $guess with your guess")


#this is how you guess for the game of high_low. The reason I go into text files here is because python doesnt like the idea of sharing variables between commands, so i have to do it myself in a roundabout way.
@client.command()
async def guess(ctx, arg):
  guess_val = int(arg)
  f = open("high_low username.txt")
  hlusername = str(f.read())
  f.close() 

  f = open("goal_number.txt")
  goal_number = int(f.read())
  f.close()

  f = open("guess_count.txt")
  guess_count = (f.read())
  f.close()   

  verification = str(ctx.message.author)
  verification = verification[-4:]

  
  if verification == hlusername:
    if guess_val > goal_number:
      await ctx.send("Lower")
      f = open("guess_count.txt")
      guess_count = int(f.read())
      f.close()    

      count_total = int(guess_count) + 1
      f = open("guess_count.txt", "w")
      f.write(str(count_total))
      f.close()

    elif guess_val < goal_number:
      await ctx.send("Higher")
      f = open("guess_count.txt")
      guess_count = int(f.read())
      f.close()   

      count_total = int(guess_count) + 1
      f = open("guess_count.txt", "w")
      f.write(str(count_total))
      f.close()

    elif guess_val == goal_number:
      guess_count = int(guess_count)
      payout = 500 - (guess_count*50)
      f = open(f"{hlusername}.txt")
      contents = int(f.read())
      f.close()

      point_total = int(contents) + payout
      f = open(f"{hlusername}.txt", "w")
      f.write(str(point_total))
      f.close()

      await ctx.send(f"You won {payout - 50} points after {guess_count} guesses")


#starts a game of blackjack
@client.command()
async def blackjack(ctx):
  list_cards = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '10', '10', '10']
  player_hand = str(random.choice(list_cards))
  dealer_hand = str(random.choice(list_cards))
  
  b_username = str(ctx.message.author)
  b_username = b_username[-4:]
  f = open("b_username.txt", "w")   
  f.write(str(b_username))
  f.close()
  
  f = open("player_hand.txt", "w")
  f.write(str(player_hand))
  f.close()

  player_hand = str(random.choice(list_cards))

  with open("player_hand.txt", "a+") as file_object:
    # Move read cursor to the start of file.
    file_object.seek(0)
    # If file is not empty then append '\n'
    data = file_object.read(100)
    if len(data) > 0 :
        file_object.write("\n")
    # Append text at the end of file
    file_object.write(str(random.choice(list_cards)))

  f = open("dealer_hand.txt", "w")
  f.write(str(dealer_hand))
  f.close()

  f = open("player_hand.txt")
  player_hand = f.readlines()
  f.close()
  
  f = open("hit_count.txt", "w")
  f.write(str(0))
  f.close()

  await ctx.send(f"You currently have {player_hand} in your hand. The dealer has a {dealer_hand} in hand and an unknown. Stand or Hit?")

def write_newline(term): 
  f = open("player_hand.txt")
  player_hand = f.readlines()
  f.close()

  list_cards = ['1', '2', '3', '4', '5', '6', '7', '8', '9','10', '10', '10', '10']

  player_hand.append(random.choice(list_cards))

  with open("player_hand.txt", "a+") as file_object:
    # Move read cursor to the start of file.
    file_object.seek(0)
    # If file is not empty then append '\n'
    data = file_object.read(100)
    if len(data) > 0 :
        file_object.write("\n")
    # Append text at the end of file
    file_object.write(player_hand[term])


#this acts as a way to hit in the game of blackjack
@client.command()
async def hit(ctx):
  
  msg_caller = str(ctx.message.author)
  msg_caller = msg_caller[-4:]

  f = open("b_username.txt")
  b_username = (f.readlines())
  f.close

  if b_username != [msg_caller]:
    await ctx.send("you didn't start this game silly")
  else:
    f = open("hit_count.txt")
    hit_count = (f.readlines())
    f.close()

    hit_count = int(hit_count[0])
    hit_count = hit_count + 1
    f = open("hit_count.txt", "w")
    f.write(str(hit_count))
    f.close()

    write_newline(int(hit_count + 1))

    f = open("player_hand.txt")
    player_hand = f.readlines()
    f.close()

    if hit_count == 1:
      p_hand_val = int(player_hand[0]) + int(player_hand[1]) + int(player_hand[2])
  
    elif hit_count == 2:
      p_hand_val = int(player_hand[0]) + int(player_hand[1]) + int(player_hand[2]) + int(player_hand[3]) 

    elif hit_count == 3:
      p_hand_val = int(player_hand[0]) + int(player_hand[1]) + int(player_hand[2]) + int(player_hand[3]) + int(player_hand[4])

    elif hit_count == 4:
      await ctx.send("You ran out of the ability to hit. This isn't a rule in blackjack, Luke just got bored here and didn't think anyone would need to hit this many times. Go harass him till he fixes it.")

    if p_hand_val > 21:
      await ctx.send(f"Your hand is {player_hand} which means you busted lol. Sucks to suck")

    elif p_hand_val < 21: 
      await ctx.send(f"Your hand is now {player_hand}. Hit or Stand?")

    elif p_hand_val == 21:
      await ctx.send(f"You hit a blackjack! You win. Very nice")


#this acts as a way to stand in the game of blackjack
@client.command()
async def stand(ctx):

  f = open("b_username.txt")
  b_username = str(f.read())
  f.close() 
  
  msg_caller = str(ctx.message.author)
  msg_caller = msg_caller[-4:]

  await ctx.send(f"{msg_caller}")
  await ctx.send(f"{b_username}")

  
  if b_username != msg_caller:
    await ctx.send("you didn't start this game silly")
  else:
    f = open("hit_count.txt")
    hit_count = str(f.readlines())
    f.close()

    f = open("player_hand.txt")
    player_hand = f.readlines()
    f.close()

    f = open("dealer_hand.txt")
    dealer_hand = f.readlines()
    f.close()

    list_cards = ['1', '2', '3', '4', '5', '6', '7', '8', '9','10', '10', '10', '10']
#this is pain
    dealer_hand.append(random.choice(list_cards))

    await ctx.send(f"The dealer's hand is {dealer_hand} before drawing to 17.")

    d_hand_val = int(dealer_hand[0])+int(dealer_hand[1])

    if d_hand_val < 17:
      dealer_hand.append(random.choice(list_cards))
      d_hand_val = int(dealer_hand[0])+int(dealer_hand[1])+int(dealer_hand[2])

      if d_hand_val < 17:
        dealer_hand.append(random.choice(list_cards))
        d_hand_val = int(dealer_hand[0])+int(dealer_hand[1])+int(dealer_hand[2])+int(dealer_hand[3])

        if d_hand_val < 17:
          dealer_hand.append(random.choice(list_cards))
          d_hand_val = int(dealer_hand[0])+int(dealer_hand[1])+int(dealer_hand[2])+int(dealer_hand[3])+int(dealer_hand[2])+int(dealer_hand[4])

          if d_hand_val < 17:
            await ctx.send(f"The dealer's hand is {dealer_hand}, and they can't hit anymore. This isn't a rule in blackjack, Luke just got bored here, so go harass him till he fixes it. ")

    p_hand_val = int(player_hand[0])+int(player_hand[1])
    if hit_count == 1:
      p_hand_val = int(player_hand[0])+int(player_hand[1])+int(player_hand[2])

    elif hit_count == 2:
      p_hand_val = int(player_hand[0])+int(player_hand[1])+int(player_hand[2])+int(player_hand[3]) 

    elif hit_count == 3:
      p_hand_val = int(player_hand[0])+int(player_hand[1])+int(player_hand[2])+int(player_hand[3])+int(player_hand[4])

    if p_hand_val >= d_hand_val:
      await ctx.send(f"You win, Good job. You had {player_hand} in hand, and the dealer had {dealer_hand} in hand. The total values were {p_hand_val} and {d_hand_val} respectively")

    elif d_hand_val > 21:
      await ctx.send(f"The dealer busted. Through no skill of your own, You managed to win. Good job I suppose. They ended up with {dealer_hand}. They had {d_hand_val} worth of points.")

    elif p_hand_val < d_hand_val:
      await ctx.send(f"You lose. You had {player_hand} in hand and the dealer had {dealer_hand}. The total values were {p_hand_val} and {d_hand_val} respectively")


@client.command()
async def pissgod(ctx):
  with open('pissgod.gif', 'rb') as f:
    picture = discord.File(f)
    await ctx.send(file=picture)
    await ctx.send("Piss lol")


@client.command()
async def fancy(ctx):
  with open('fancy.png', 'rb') as f:
    picture = discord.File(f)
    await ctx.send(file=picture)

@client.command()
async def no(ctx):
  with open('No.png', 'rb') as f:
    picture = discord.File(f)
    await ctx.send(file=picture)


@client.command()
async def tableflip(ctx):

  f = open("flipped?.txt")
  flipped = (f.readlines())
  f.close()

  if flipped == ['0']:
    await ctx.send("(╯°□°）╯︵ ┻━┻")

    f = open("flipped?.txt", 'w')
    f.write(str(1))
    f.close()

  elif flipped == ['1']:
    await ctx.send("The table is already flipped.") 


@client.command()
async def unflip(ctx):
  f = open("flipped?.txt")
  flipped = (f.readlines())
  f.close()

  if flipped == ['1']:
    await ctx.send("┬─┬ ノ( ゜-゜ノ)")

    f = open("flipped?.txt", 'w')
    f.write(str(0))
    f.close()

  if flipped == ['0']:
    await ctx.send("The table is already right side up.") 


@client.command()
async def randcolor(ctx): 

  random_number = random.randint(0,16777215)
  hex_number = str(hex(random_number))
  hex_number = hex_number[2:]

  #url = requests.get(f"https://www.colorhexa.com/{hex_number}")

  #soup = BeautifulSoup(url.content, "html.parser")

  #description = soup.find(class_="tb").text

  #await ctx.send(f"A complementary color is {description}.")

  await ctx.send(f"https://www.colorhexa.com/{hex_number}")



@client.command()
async def convert(ctx, arg1, arg2):

#1 km is 0.62137119223733 miles
#1 mile is 1 km divided by 0.62137119223733
#1 meter is 3.2808 feet
#1 foot is 1 meter divided by 3.2808
  unit_type = arg1
  unit_val = float(arg2)

  if unit_type == "km-mi":

    converted_val = unit_val * 0.62137
    await ctx.send(f"{unit_val} km is equal to {converted_val} mi")
  
  if unit_type == "mi-km":

    converted_val = unit_val / 0.62137
    await ctx.send(f"{unit_val} mi is equal to {converted_val} km")

  if unit_type == "m-ft":

    converted_val = unit_val * 3.2808
    await ctx.send(f"{unit_val} m is equal to {converted_val} ft")

  if unit_type == "ft-m":

    converted_val = unit_val/3.2808
    await ctx.send(f"{unit_val} ft is equal to {converted_val} m")


@client.command()
async def rps(ctx, arg):
  player_shape = str(arg)
  #1 is rock, 2 is paper, and 3 is scissors
  computer_hand = random.randint(1, 3)
  
  if player_shape == "rock":

      if computer_hand == 1:
          await ctx.send("I chose rock, so its a tie.")

      elif computer_hand == 2:
          await ctx.send("I chose paper, so I win nerd.")

      elif computer_hand == 3:
          await ctx.send("I chose scissors, so I lost. I'll beat you next time though.")

  elif player_shape == "paper":

      if computer_hand == 1:
          await ctx.send("I chose rock, so you win. Paper is a choice for little babys. Just saying.")

      elif computer_hand == 2:
          await ctx.send("I chose paper, so we tie. Paper sure is a boring choice")

      elif computer_hand == 3:
          await ctx.send("I chose scissors, so I win. See, that's what you get for choosing paper.")

  elif player_shape == "scissors":

      if computer_hand == 1:
          await ctx.send("I chose rock, so I crush your scissors with my rock.")

      elif computer_hand == 2:
          await ctx.send("I chose paper, so I get viscerally sliced in half. Is that what you wanted on your consience? Murder?")
  
      elif computer_hand == 3:
          await ctx.send("I chose scissors, so we tie. play again please. im bored.")

keep_alive()
client.run('ODM5MjEzMDQxMzQxMzAwNzM2.YJGYDA.XW3WhV67CZkYl_1e9PiH1W2T3es')
