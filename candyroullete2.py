import time
import random

class Logic_candy():    # Для логики третьего уровня
    def __init__(self, think: bool, sure: bool = False):
        self.think = think
        self.sure = sure
class Opponent():
    def __init__(self, lives: int, difficulty: int, items: list[str] = None):
        self.lives = lives
        self.max_lives = lives
        self.difficulty = difficulty
        self.items = items
        self.think_candies = []
        self.sour_total = 0
        self.sweet_total = 0
    
    def play(self, current_candies: list[bool], player_items: list[str], player_jailed: bool, refresh_think = False) -> tuple[str, bool]: # возвращает предмет и/или кому он хочет дать конфету
        if self.difficulty == 0:    # рандомизатор
            item_choice = ""
            if self.items != []:
                item_choice = random.choice[self.items]
            return (item_choice, random.choice([True, False]))
        elif self.difficulty == 1:  # нубик
            if refresh_think:
                self.think_candies = []
                for i in current_candies:
                    self.think_candies.append(random.choice([True, False]))
            self.sour_total = current_candies.count(True)
            self.sweet_total = current_candies.count(False)
            if self.sour_total == 0 or self.sweet_total == 0:
                self.think_candies = []
                for i in current_candies:
                    self.think_candies.append(i)
            # поедательная логика
            if self.think_candies[0] == False:
                give_player = False
            elif self.think_candies[0] == True:
                give_player = True
            # предметная логика (определяет если конфета идет и какие предметы)
            if self.items != []:
                if "Чай" in self.items:
                    if player_items != [] and player_items.count("Чай") != len(player_items):
                        return ("Чай", False)
                if "Тестер" in self.items:
                    if self.sour_total != 0 and self.sweet_total != 0:
                        self.think_candies[0] = current_candies[0]
                        return("Тестер", False)
                if "Телефон" in self.items:
                    if len(self.think_candies) > 1: 
                        index_phone, sour_phone = game_handler.phone_logic()
                        self.think_candies[index_phone] = sour_phone
                        return ("Телефон", False)
                if "Кока-кола" in self.items:
                    if self.sour_total != 0 and self.sweet_total != 0:
                        if random.choice([True, False]):
                            return("Кока-кола", False)
                if "Шоколад" in self.items:
                    if self.lives < self.max_lives:
                        return("Шоколад", False)
                if "Молоко" in self.items:
                    if self.lives < self.max_lives-1:
                        return("Молоко", False)
                if "Усилитель" in self.items:
                    if self.think_candies[0] == True:
                        return ("Усилитель", True)
                if "Инвертер" in self.items:
                    if self.think_candies[0] == False:
                        self.think_candies[0] = True
                        return ("Инвертер", True)
                if "Наручники" in self.items:
                    if self.think_candies[0] and player_jailed == False:
                        return("Наручники", True)
            return ("", give_player)
        elif self.difficulty == 2:  # про
            if refresh_think:
                self.think_candies = []
                current_candies2 = current_candies
                for i in current_candies:
                    self.think_candies.append(Logic_candy(current_candies2.pop(random.randint(0, len(current_candies2)-1)), False))
            self.sour_total = self.think_candies.count(Logic_candy(True, False))
            self.sweet_total = self.think_candies.count(Logic_candy(False, False))
            for i in self.think_candies:
                if i.sure:
                    pass
                else:
                    unsure_candies_bool = []
                    for i in range(self.sour_total):
                        unsure_candies_bool.append(True)
                    for i in range(self.sweet_total):
                        unsure_candies_bool.append(False)
                    if unsure_candies_bool.count(True) > unsure_candies_bool.count(False):
                        i.think = True
                        unsure_candies_bool.remove(True)
                    else:
                        i.think = False
                        unsure_candies_bool.remove(False)
            # поедательная логика
            if self.think_candies[0].think == False:
                give_player = False
            elif self.think_candies[0].think == True:
                give_player = True
            if self.items != []:
                if "Чай" in self.items:
                    if player_items != [] and player_items.count("Чай") != len(player_items) and self.steal(player_items) != False:
                        return ("Чай", False)
                if "Тестер" in self.items:
                    if self.sour_total != 0 and self.sweet_total != 0:
                        self.think_candies[0] = current_candies[0]
                        return("Тестер", False)
                if "Телефон" in self.items:
                    if len(self.think_candies) > 1: 
                        index_phone, sour_phone = game_handler.phone_logic()
                        self.think_candies[index_phone].think = sour_phone
                        self.think_candies[index_phone].sure = True
                        return ("Телефон", False)
                if "Кока-кола" in self.items:
                    if self.think_candies[0].sure == False:
                        if random.choice([True, False]):
                            return("Кока-кола", False)
                if "Шоколад" in self.items:
                    if self.lives < self.max_lives:
                        return("Шоколад", False)
                if "Молоко" in self.items:
                    if self.lives < self.max_lives-1:
                        return("Молоко", False)
                if "Усилитель" in self.items:
                    if self.think_candies[0] == True:
                        return ("Усилитель", True)
                if "Инвертер" in self.items:
                    if self.think_candies[0] == False:
                        return ("Инвертер", False)
                if "Наручники" in self.items:
                    if self.think_candies[0] and player_jailed == False:
                        return("Наручники", False)
            return ("", give_player)
        
        elif self.difficulty == 3:  # хакер
            if current_candies[0]:
                give_player = True
            else:
                give_player = False
            if self.items != []:
                if "Тестер" in self.items:
                    return("Тестер", False)
                if "Телефон" in self.items:
                    return ("Телефон", False)
                if "Чай" in self.items:
                    if player_items != [] and player_items.count("Чай") != len(player_items):
                        if self.steal(player_items) != False:
                            return ("Чай", False)
                if "Кока-кола" in self.items:
                    if current_candies[0] == False:
                        return("Кока-кола", False)
                if "Шоколад" in self.items:
                    if self.lives < self.max_lives:
                        return("Шоколад", False)
                if "Молоко" in self.items:
                    if self.lives < self.max_lives-1:
                        return("Молоко", False)
                if "Усилитель" in self.items:
                    if current_candies[0] == True:
                        return ("Усилитель", True)
                if "Инвертер" in self.items:
                    if current_candies[0] == False:
                        return ("Инвертер", False)
                if "Наручники" in self.items:
                    if player_jailed == False:
                        return("Наручники", True)
    def steal(self, player_items: list[str]) -> str:     # румыния
        if self.difficulty == 0:    # раномизатор
            return random.choice(player_items)
        elif self.difficulty == 1:  # по приоритету
            priority_list = {
                "Усилитель": 4,
                "Инвертер": 3.5,
                "Телефон": 2.5,
                "Тестер": 5,
                "Кока-кола": 2,
                "Шоколад": 5,
                "Молоко": 4,
                "Наручники": 4.5,
                "Чай": -1
            }
            pick = [0, "None"]
            for i in player_items:
                if priority_list[i] > pick[0]:
                    pick = [priority_list[i], i]
                elif priority_list[i] == pick[0]:
                    if random.randint(0, 1):
                        pick = [priority_list[i], i]
            return pick[1]
        elif self.difficulty == 2:  # пипец он умный
            if "Усилитель" in player_items and (self.think_candies[0].think or self.think_candies[0].think == False and "Ивертер" in self.items):
                return "Усилитель"
            elif "Инвертер" in player_items and (self.think_candies[0].think == False):
                return "Инвертер"
            elif "Тестер" in player_items and self.think_candies[0].sure == False:
                return "Тестер"
            elif "Кока-кола" in player_items and self.think_candies[0].sure == False:
                return "Кока-кола"
            elif "Шоколад" in player_items and self.lives < self.max_lives:
                return "Шоколад"
            elif "Молоко" in player_items and self.lives == 1 and self.think_candies[0].sure == False:
                return "Молоко"
            elif "Наручники" in player_items:
                return "Наручники"
            else:
                return False
            
        elif self.difficulty == 3:  # про но не берет инфу потомучто супер умный
            if "Усилитель" in player_items and (self.think_candies[0] or self.think_candies[0] == False and "Ивертер" in self.items):
                return "Усилитель"
            elif "Инвертер" in player_items and (self.think_candies[0] == False):
                return "Инвертер"
            elif "Шоколад" in player_items and self.lives < self.max_lives:
                return "Шоколад"
            elif "Молоко" in player_items and self.lives == 1 and self.think_candies[0] == False:
                return "Молоко"
            elif "Наручники" in player_items:
                return "Наручники"
            else:
                return False


class Player():
    def __init__(self, lives: int, items: list[str]):
        self.lives = lives
        self.items = items
        self.max_lives = lives
    
    def get_input(self, enemy_lives: int, enemy_items: list[str]):
        global game_handler
        typewriter_display(f"Ваш ход. Жизни: {self.lives}. Инвентарь: ")
        for i, item in enumerate(self.items):
            if i != len(self.items)-1:
                typewriter_display(f"{item}, ")
            else:
                typewriter_display(f"{item}.\n")
        while True:
            typewriter_display("\n1. Проверить оппонента.\n2. Использовать предмет\n3. Дать конфету.\n0. Меню\n")
            player_input = input(">>> ")
            if "1" in player_input:
                typewriter_display(f"\nЖизни оппонента: {enemy_lives}. Предметы: ")
                for i, item in enumerate(enemy_items):
                    if i != len(self.items)-1:
                        typewriter_display(f"{item}, ")
                    else:
                        typewriter_display(f"{item}.\n")
            elif "2" in player_input:
                while True:
                    typewriter_display("Какой предмет вы желаете использовать:\n")
                    i = -1
                    for i, n in enumerate(self.items):
                        typewriter_display(f"{i}. {n}\n")
                    typewriter_display(f"{i+1}. Вернуться\n")
                    try:
                        player_input = int(input(">>> "))
                    except:
                        break
                    if player_input == i+1:
                        break
                    elif player_input < len(self.items):
                        return (self.items[i], False)
            elif "3" in player_input:
                while True:
                    typewriter_display("Кому вы хотите дать конфету?\n1. Себе\n2. Оппоненту\n0. Вернуться\n")
                    player_input = input(">>> ")
                    if "1" in player_input:
                        return ("", False)
                    elif "2" in player_input:
                        return ("", True)
                    elif "0" in player_input:
                        break
            elif "0" in player_input:
                while True:
                    typewriter_display("1. Настройки.\n2. Выход.\n0. Обратно к игре.\n")
                    player_input = input(">>> ")
                    if "1" in player_input:
                        open_menu()
                    if "2" in player_input:
                        while True:
                            typewriter_display("Вы уверены?\n1. Да\n2. Нет.")
                            player_input = input(">>> ")
                            if "1" in player_input:
                                game_handler.end_game
                            else:
                                break
                    elif "0" in player_input:
                        break
    def get_steal(self, enemy_items: list[str]) -> str:
        while True:
            typewriter_display("Какой предмет вы желаете украсть:\n")
            for i, n in enumerate(enemy_items):
                typewriter_display(f"{i}. {n}\n")
                typewriter_display(f"{i+1}. Вернуться\n")
            try:
                player_input = int(input(">>> "))
            except:
                pass
            if player_input < len(enemy_items):
                return (enemy_items[i])

class Game_handler():
    def __init__(self):
        self.round = 0
        self.candies = []
        self.player_turn = True

    def new_game(self, difficulty):
        global game_running
        game_running = True
        self.round = 1
        self.difficulty = difficulty
        self.new_round()

    def new_round(self):
        self.refresh_ran = False
        if self.round == 1:
            self.candy_gen(2, 3)
            self.opponent = Opponent(2, self.difficulty, [])
            self.player = Player(2, [])
        if self.round == 2:
            self.candy_gen(2, 8)
            self.opponent = Opponent(3, self.difficulty, [])
            self.player = Player(3, [])
            self.item_gen(2)
        if self.round == 3:
            self.candy_gen(2, 8)
            self.opponent = Opponent(4, self.difficulty, [])
            self.player = Player(4, [])
            self.item_gen(4)
        if self.round == 4:
            self.end_game()
    def end_game(self):
        global game_running, game_end
        game_running = False
        game_end = True
        if self.round == 4:
            if self.difficulty == 1:
                achievements["ez_pz"] = True
            if self.difficulty == 2:
                achievements["normal_this"] = True
            if self.difficulty == 3:
                achievements["a_true_battle"] = True
            if self.difficulty == 4:
                achievements["omg_u_hax0r"] = True
    def candy_gen(self, min: int, max: int):
                total_candies = random.randint(min, max)
                self.candies = []
                self.double_damage = False
                self.skip_turn_player = False
                self.skip_turn_opp = False
                for i in range(total_candies):
                    self.candies.append(random.choice([True, False]))
                if self.candies.count(True) == len(self.candies):
                    self.candies[random.randint(0, total_candies-1)] = False
                elif self.candies.count(False) == len(self.candies):
                    self.candies[random.randint(0, total_candies-1)] = True
                typewriter_display(text["new_round"].format(len(self.candies), self.candies.count(True), self.candies.count(False)))
    def item_gen(self, amount):
        global items
        for i in range(amount):
            self.player.items.append(random.choice(items))
        for i in range(amount):
            self.opponent.items.append(random.choice(items))
    def play(self):
        if self.player_turn:
            item, enemy = self.player.get_input(self.opponent.lives, self.opponent.items)
            if item == "":
                if enemy:
                    if self.candies[0]:
                        self.opponent.lives -= 1 + 1*bool(self.double_damage)
                        typewriter_display(text["sour_player_opp"].format(self.opponent.lives))
                        self.candies.pop(0)
                        self.player_turn = False

                    else:
                        typewriter_display(text["sweet_player_opp"])
                        self.candies.pop(0)
                        self.player_turn = False
                else:
                    if self.candies[0]:
                        self.player.lives -= 1 + 1*bool(self.double_damage)
                        typewriter_display(text["sour_player_self"].format(self.player.lives))
                        self.candies.pop(0)
                        self.player_turn = False
                    else:
                        typewriter_display(text["sweet_player_self"])
                        self.candies.pop(0)
                self.double_damage = False
            else:
                if item == "Усилитель":
                    typewriter_display(text[("Усилитель", False)])
                    self.double_damage = True
                    self.player.items.remove("Усилитель")
                elif item == "Инвертер":
                    typewriter_display(text[("Инвертер", False)])
                    self.candies[0] = not self.candies[0]
                    self.player.items.remove("Инвертер")
                elif item == "Телефон":
                    typewriter_display(text[("Телефон", False)])
                    ind, sr = self.phone_logic()
                    if ind != -1:
                        if sr:
                            typewriter_display(f"{ind}-ая конфета кислая\n")
                        else:
                            typewriter_display(f"{ind}-ая конфета сладкая\n")
                    else:
                        typewriter_display(f"Как неудачно...")
                    self.player.items.remove("Телефон")
                elif item == "Тестер":
                    if self.candies[0]:
                        tmp_candy = "Кислая"
                    else:
                        tmp_candy = "Сладкая"
                    typewriter_display(text[("Тестер", False)].format(tmp_candy))
                    self.player.items.remove("Тестер")
                elif item == "Кока-кола":
                    typewriter_display(text[("Кока-кола", False)])
                    if self.candies[0]:
                        typewriter_display("Она была кислой!")
                    else:
                        typewriter_display("Она была сладкой!")
                    self.candies.pop(0)
                    self.player.items.remove("Кока-кола")
                elif item == "Шоколад":
                    if self.player.lives != self.player.max_lives:
                        self.player.lives += 1
                        typewriter_display(text[("Шоколад", False)]).format(self.player.lives)
                        self.player.items.remove("Шоколад")
                    else:
                        typewriter_display("У вас уже максимальное количество жизней!")
                elif item == "Молоко":
                    tmp = random.randchoice(["просрочено", "свежее"])
                    if tmp == "просрочено":
                        self.player.lives -= 1
                        typewriter_display(text[("Молоко", False)]).format(tmp, self.player.lives)
                    else:
                        self.player.lives += 2
                        if self.player.lives > self.player.max_lives:
                            self.player.lives = self.player.max_lives
                        typewriter_display(text[("Молоко", False)]).format(tmp, self.player.lives)
                    self.player.items.remove("Молоко")
                elif item == "Наручники":
                    if not self.skip_turn_opp:
                        typewriter_display(text[("Наручники", False)])
                        self.skip_turn_opp = True
                        self.player.items.remove("Наручники")
                elif item == "Чай":
                    if self.opponent.items != []:
                        typewriter_display(text[("Чай", False)])
                        stolen = self.player.get_steal(self.opponent.items)
                        self.player.items.append(stolen)
                        self.player.items.remove("Чай")
                        self.opponent.items.remove(stolen)
        else:
            if self.refresh_ran:
                item, enemy = self.opponent.play(self.candies, self.player.items, self.skip_turn_player, False)
            else:
                item, enemy = self.opponent.play(self.candies, self.player.items, self.skip_turn_player, True)
                self.refresh_ran = True
            if item == "":
                if enemy:
                    if self.candies[0]:
                        self.player.lives -= 1 + 1*bool(self.double_damage)
                        typewriter_display(text["sour_opp_player"].format(self.player.lives))
                        self.candies.pop(0)
                        self.player_turn = True

                    else:
                        typewriter_display(text["sweet_opp_player"])
                        self.candies.pop(0)
                        self.player_turn = True
                else:
                    if self.candies[0]:
                        self.opponent.lives -= 1 + 1*bool(self.double_damage)
                        typewriter_display(text["sour_opp_self"].format(self.opponent.lives))
                        self.candies.pop(0)
                        self.player_turn = True
                    else:
                        typewriter_display(text["sweet_opp_self"])
                        self.candies.pop(0)
                self.double_damage = False
            else:
                if item == "Усилитель":
                    typewriter_display(text[("Усилитель", True)])
                    self.double_damage = True
                    self.opponent.items.remove("Усилитель")
                elif item == "Инвертер":
                    typewriter_display(text[("Инвертер", True)])
                    self.candies[0] = not self.candies[0]
                    self.opponent.items.remove("Инвертер")
                elif item == "Телефон":
                    typewriter_display(text[("Телефон", True)])
                    self.opponent.items.remove("Телефон")
                elif item == "Тестер":
                    typewriter_display(text[("Тестер", True)])
                    self.opponent.items.remove("Тестер")
                elif item == "Кока-кола":
                    typewriter_display(text[("Кока-кола", True)])
                    if self.candies[0]:
                        typewriter_display("Она была кислой!")
                    else:
                        typewriter_display("Она была сладкой!")
                    self.candies.pop(0)
                    self.opponent.items.remove("Кока-кола")
                elif item == "Шоколад":
                    self.opponent.lives += 1
                    typewriter_display(text[("Шоколад", True)]).format(self.opponent.lives)
                    self.opponent.items.remove("Шоколад")
                elif item == "Молоко":
                    tmp = random.choice(["просрочено", "свежее"])
                    if tmp == "просрочено":
                        self.opponent.lives -= 1
                        typewriter_display(text[("Молоко", True)]).format(tmp, self.opponent.lives)
                    else:
                        self.opponent.lives += 2
                        if self.opponent.lives > self.opponent.max_lives:
                            self.opponent.lives = self.opponent.max_lives
                        typewriter_display(text[("Молоко", True)]).format(tmp, self.opponent.lives)
                    self.player.items.remove("Молоко")
                elif item == "Наручники":
                    typewriter_display(text[("Наручники", True)])
                    self.skip_turn_player = True
                    self.opponent.items.remove("Наручники")
                elif item == "Чай":
                    if self.opponent.items != []:
                        stolen = self.opponent.steal(self.player.items)
                        typewriter_display(text[("Чай", True)].format(stolen))
                        self.opponent.items.append(stolen)
                        self.opponent.items.remove("Чай")
                        self.player.items.remove(stolen)
    def end_of_action_update(self):
        if self.opponent.lives == 0:
            self.round += 1
            typewriter_display(f"Вы победили! Раунд: {self.round}\n")
            self.new_round()
            self.player_turn = True
        elif self.player.lives == 0:
            typewriter_display(f"Вы проиграли. Последний раунд: {self.round}\n")
            self.end_game()
            self.player_turn = True
        if len(self.candies) == 0 and self.opponent.lives > 0 and self.player.lives > 0:
            self.candy_gen(2, 8)
            self.player_turn = True
        if self.skip_turn_player and self.player_turn:
            self.skip_turn_player = False
            self.player_turn = False
        if self.skip_turn_opp and not self.player_turn:
            self.skip_turn_opp == False
            self.player_turn = True
            print("override!")
        

    def phone_logic(self) -> tuple[int, bool]:
        if len(self.candies) > 1:
            index = random.choice(range(1, len(self.candies)))+1
            sour = self.candies[index-1]
        else:
            index = None
            sour = False
        return (index, sour)


def typewriter_display(text: str, secs: float = 0.05) -> None:
    # Функция берет текст и выводит каждый символ поочереди с интервалом в secs секунд.
    # Символ * обозначает начало паузы, внутри двух * обозначается время паузы. Пример: "Я... *1.4* Стив" - сделает паузу 1.4 секунд во время вывода.
    global time_multiplier
    while text != "":
        if text[0] != "*":
            print(text[0], flush=True, end="")
            time.sleep(secs*time_multiplier)
            text = text[1:]
        else:
            try:
                text = text[1:]
                temp_storage = ""
                while text[0] != "*":
                    temp_storage += text[0]
                    text = text[1:]
                time.sleep(float(temp_storage)*time_multiplier)
                text = text[1:]
            except:
                raise SyntaxError("Введен некорректный текст!")

def save() -> None:
    new_save = open("save.txt", "w")
    new_data = ""
    for i in stats:
        new_data += str(stats[i])
        new_data += "\n"
    for i in achievements:
        new_data += str(achievements[i])
        new_data += "\n"
    new_data += str(time_multiplier)
    new_save.writelines(new_data)

def open_menu() -> None:
    global time_multiplier
    while True:
        typewriter_display("Настройки:\n1. Скорость текста\n0. Выход", 0.05)
        menu_input = input("\n>>> ")
        if "1" in menu_input:
            while True:
                typewriter_display("Введите скорость появления текста (0-2, где 0 - мгновенно, 2 - в два раза медленнее)\n", 0.05)
                menu_input = input(">>> ")
                try:
                    menu_input = float(menu_input)
                    if 0 <= menu_input <= 2:
                        time_multiplier =  menu_input
                        break
                    else:
                        typewriter_display("Введите число между 0 и 2!")
                except:
                    typewriter_display(f"\"{menu_input}\" не является числом! \n", 0.05)
                    if "," in menu_input:
                        typewriter_display("Чтобы ввести нецелые числа используйте точку. \n", 0.05)
        elif "0" in menu_input:
            break



try:
    open("save.txt", "r")
    new_file = False
except:
    open("save.txt", "x")
    new_file = True
if new_file:
    stats = {
        "tea_consumed": 0,
        "cola_consumed": 0,
        "milk_consumed": 0,
        "sour_eaten": 0,
        "sweet_eaten": 0,
        "sour_given": 0,
        "sweet_given": 0,
        "rounds_won": 0,
        "rounds_lost": 0,
        "max_score": 0
    }
    achievements = {
        "dehydrated": False,    # Не использовать чай, колу или молоко.
        "sweet_tooth": False,   # Выпить чай, молоко, сладкую конфету, шоколад за 1 ход.
        "gambler_curse": False, # Получить урон от молока 3 раза за одну игру
        "wombo_combo": False, # Использовать тестер, инвертер, усилитель за один ход
        "ez_pz": False, # Пройти простого бота
        "normal_this": False, # Пройти среднего бота
        "a_true_battle": False, # Пройти сложного бота
        "omg_u_hax0r": False, # Пройти невозможного бота
    }
    time_multiplier = 1
else:
    save_data = open("save.txt", "r")
    save_data = save_data.readlines()
    for i, n in enumerate(save_data):
        try:
            save_data[i] = float(n.replace("\n", ""))
        except:
            save_data[i] = n.replace("\n", "")
            if save_data[i] == "False": save_data[i] = False
            else: save_data[i] = True
    stats = {
        "tea_consumed": save_data[0],
        "cola_consumed": save_data[1],
        "milk_consumed": save_data[2],
        "sour_eaten": save_data[3],
        "sweet_eaten": save_data[4],
        "sour_given": save_data[5],
        "sweet_given": save_data[6],
        "rounds_won": save_data[7],
        "rounds_lost": save_data[8],
        "max_score": save_data[9]
    }
    achievements = {
        "dehydrated": save_data[10],    # Не использовать чай, колу или молоко.
        "sweet_tooth": save_data[11],   # Выпить чай, молоко, сладкую конфету, шоколад за 1 ход.
        "gambler_curse": save_data[12], # Получить урон от молока 3 раза за одну игру
        "wombo_combo": save_data[13], # Использовать тестер, инвертер, усилитель за один ход
        "ez_pz": save_data[14], # Пройти простого бота
        "normal_this": save_data[15], # Пройти среднего бота
        "a_true_battle": save_data[16], # Пройти сложного бота
        "omg_u_hax0r": save_data[17], # Пройти невозможного бота
    }
    time_multiplier = save_data[18]
save()


text = {
    "new_round": "{} конфет(ы), {} кислые, {} сладкие.\n",
    "sour_player_self": "Вы кладете конфету в рот. *2*Конфета кислая. Жизни: {}\n",
    "sour_opp_self": "Противник кладет конфету в рот. *2*Конфета кислая. Жизни противника: {}\n",
    "sour_player_opp": "Вы даете противнику конфету. *2*Конфета кислая. Жизни противника: {}\n",
    "sour_opp_player": "Противник дает вам конфету. *2*Конфета кислая. Жизни: {}\n",
    "sweet_player_self": "Вы кладете конфету в рот. *2*Конфета сладкая.\n",
    "sweet_opp_self": "Противник кладет конфету в рот. *2*Конфета сладкая.\n",
    "sweet_player_opp": "Вы даете противнику конфету. *2*Конфета сладкая.\n",
    "sweet_opp_player": "Противник дает вам конфету. *2*Конфета сладкая.\n",
    ("Усилитель", True): "Противник заряжает конфету усилителем.\n",
    ("Инвертер", True): "Противник обращает кислость конфеты.\n",
    ("Телефон", True): "Противник звонит по телефону и получает информацию.\n",
    ("Тестер", True): "Противник проверяет кислость конфеты\n",
    ("Кока-кола", True): "Противник пьет кока-колу и выбрасывает конфету.\n",
    ("Шоколад", True): "Противник ест плитку шоколада. Жизни противника: {}\n",
    ("Молоко", True): "Противник пьет молоко... *2*Оно {}. Жизни противника: {}\n",
    ("Наручники", True): "Противник дает вам наручники. Ваш следующий ход будет пропущен.\n",
    ("Чай", True): "Противник пьет чай и крадет у вас.*0.4*.*0.7*.*1* {}\n",
    "player_skip": "Ваш ход пропускается так как вы в наручниках.\n",
    ("Усилитель", False): "Вы используете усилитель на конфету.\n",
    ("Инвертер", False): "Вы обращаете конфету инвертером.\n",
    ("Телефон", False): "Вы достаете телефон...\n",
    ("Тестер", False): "Вы тестируете конфету. Она {}.\n",
    ("Кока-кола", False): "Вы пьете кока-колу и выбрасываете конфету.\n",
    ("Шоколад", False): "Вы берете плитку шоколада. Ваши жизни: {}\n",
    ("Молоко", False): "Вы пьете молоко...*2* Оно {}. Ваши жизни: {}\n",
    ("Наручники", False): "Вы даете противнику наручники.\n",
    ("Чай", False): "Вы пьете чай... Ваше сердцебиение учащается, вы можете украсть один предмет.\n",
    "opp_skip": "Ход противника пропускается так как он в наручниках.\n",
}
items = [
    "Усилитель",    # Увеличивает урон кислых конфет в 2 раза, не имеет эффекта на сладкие конфеты
    "Инвертер",     # Инвертирует конфету. Кислая -> сладкая, сладкая -> кислая.
    "Телефон",      # Дает информацию о случайной конфете. Не работает при одной конфете.
    "Тестер",       # Дает информация о текущей конфете.
    "Кока-кола",    # Убирает конфету, не тратя на это ход.
    "Шоколад",      # Дает 1 жизнь.
    "Молоко",       # 50% - 2 жизни, 50% - -1 жизнь.
    "Наручники",    # Нуллифицирует следующий ход противника.
    "Чай"           # Дает украсть предмет у противника.
]
game_handler = Game_handler()
game_running = False
game_end = False

typewriter_display("==========================================\n          К*0.15*о*0.15*н*0.15*ф*0.15*е*0.15*т*0.15*н*0.15*а*0.15*я*0.15* р*0.15*у*0.15*л*0.15*е*0.15*т*0.15*к*0.15*а\n", 0)
while True:
    typewriter_display("1. Выбор игры\n2. Настройки\n3. Достижения и статистика\n0. Выход\n", 0.1)
    menu_input = input(">>> ")
    if "1" in menu_input:
        while True:
            typewriter_display("Выберите сложность противника:\n", 0.05)
            typewriter_display("1. Простой\n- Самый простой и непредсказуемый противник. Действует случайно, не имеет стратегии.\n", 0.05)
            typewriter_display("2. Средний\n- Базовый противник. Имеет что-то напоминающее стратегию.\n", 0.05)
            if achievements["normal_this"]:
                typewriter_display("3. Сложный\n- Настоящий противник. Имеет продвинутую стратегию, не для новичков.\n", 0.05)
            else:
                typewriter_display("3. Сложный\n- Закрыто! Пройдите среднего противника чтобы разблокировать.\n", 0.05)
            if achievements["a_true_battle"]:
                typewriter_display("4. Невозможный\n- Нечестно! Использует больше информации, чем ему дано. Не рекомендовано для игры.\n", 0.05)
            else:
                typewriter_display("4. Невозможный\n- Закрыто! Пройдите сложного противника чтобы разблокировать.\n", 0.05)
            menu_input = input(">>> ")
            try:
                menu_input = int(menu_input)
            except:
                pass    
            if 0 < menu_input < 3:
                game_handler.new_game(1)
            elif menu_input == 3:
                if achievements["normal_this"]:
                    game_handler.new_game(menu_input-1)
                else:
                    typewriter_display("Данная сложность еще не разблокирована!", 0.05)
            elif menu_input == 4:
                if achievements["a_true_battle"]:
                    game_handler.new_game(menu_input-1)
                else:
                    typewriter_display("Данная сложность еще не разблокирована!", 0.05)
            while game_running:
                game_handler.play()
                game_handler.end_of_action_update()
            if game_end:
                game_end = False
                break


    elif "2" in menu_input:
        open_menu()
    elif "3" in menu_input:
        while True:
            typewriter_display("Достижения и статистика будут добавлены позже!", 0.05)
    elif "0" in menu_input:
        break
save()
