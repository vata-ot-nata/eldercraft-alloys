# 1 - золото, 2 - железо, 3 - алмаз, 4 - незерит, 5 - медь, 6 - метеорит
mass = [1.6, 2.4, 3, 3.5,  2.3]
speed = [2.4, 1.6, 1, 0.5, 1.7]
damage = [2, 6, 8, 12, 5]

best_weapon_proportions = [0, 0, 0, 0, 0]
best_rapier_proportions = [0, 0, 0, 0, 0]

# 1 - урон/сек, 2 - урон, 3 - скорость атаки, 4 - вес
best_weapon_stats = [0, 0, 0, 0]
best_rapier_stats = [0, 0, 0, 0]

# считает неэффективно, считает и невозможные сплавы (которые слабее, чем обычные).
# Например, сплав из 3 слитков: 1 железа и 1 золота.
# Но я их отсекаю, так что на результат это не влияет,
# а влияет только на скорость вычислений.
# Так что всё равно
for n in range(1, 9+1): # проход по всем кол-вам металлов в сплаве
    for x in range(n + 1): # золото
        for y in range(n - x + 1):  # железо
            for z in range(n - x - y + 1):  # алмаз
                for w in range(n - x - y - z + 1):  # незерит
                    for v in range(n  - x - y - z - w + 1):  # медь
                        if x+y+z+w+v == n: # если сплав возможен
                            pm = [x/n, y/n, z/n, w/n, v/n] # пропорции металлов в сплаве
                            apm = [x, y, z, w, v] # абсолютные значния металлов в сплаве

                            stat_mass = pm[0]*mass[0] + pm[1]*mass[1] + pm[2]*mass[2] + pm[3]*mass[3] + pm[4]*mass[4]
                            stat_damage = pm[0]*damage[0] + pm[1]*damage[1] + pm[2]*damage[2] + pm[3]*damage[3] + pm[4]*damage[4]
                            stat_speed = pm[0]*speed[0] + pm[1]*speed[1] + pm[2]*speed[2] + pm[3]*speed[3] + pm[4]*speed[4]
                            stat_dps = stat_damage*stat_speed # урон/сек


                            sec = max((20/5), 20-((4*stat_damage)/(min(4, 20)+8)))
                            tocheck = stat_speed*(stat_damage*(1-(min(20, sec))/25))
                            # проверка самого крутого оружия
                            if tocheck > best_weapon_stats[0]:
                                best_weapon_proportions = apm
                                best_weapon_stats = [tocheck, stat_damage, stat_speed, stat_mass]

                            # проверка самой крутой рапиры
                            if stat_mass < 2.287: # если вес соответсвует рапире
                                if tocheck > best_rapier_stats[1]:
                                    best_rapier_proportions = apm
                                    best_rapier_stats = [tocheck, stat_damage, stat_speed, stat_mass]


print("Сплав лучшего оружия:",
      best_weapon_proportions[0], "золота",
      best_weapon_proportions[1], "железа",
      best_weapon_proportions[2], "алмазов",
      best_weapon_proportions[3], "незерита",
      best_weapon_proportions[4], "меди")
print("Его статы:",
      best_weapon_stats[0], "урона/сек",
      best_weapon_stats[1], "урона",
      best_weapon_stats[2], "скорости атаки",
      best_weapon_stats[3], "веса")

print("Лучшая шпага:",
      best_rapier_proportions[0], "золота",
      best_rapier_proportions[1], "железа",
      best_rapier_proportions[2], "алмазов",
      best_rapier_proportions[3], "незерита",
      best_rapier_proportions[4], "меди")
print("Её статы:",
      best_rapier_stats[0], "урона/сек",
      best_rapier_stats[1], "урона",
      best_rapier_stats[2], "скорости атаки",
      best_rapier_stats[3], "веса")