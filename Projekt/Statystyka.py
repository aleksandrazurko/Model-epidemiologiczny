import scipy.stats as st
import numpy as np
import matplotlib.pyplot as plt
import os

# wczytanie pliku z symulacją
def loadfile(filename):
    with open(filename):
        allIn, illIn, infectedOut, allOut, mask = np.genfromtxt(filename, dtype = int, delimiter = ',', skip_header=12, unpack = True, usecols = range(0, 5))
    return allIn, illIn, infectedOut, allOut, mask

# rysuje histogramy wyników z symulacji
# jako parametry trzeba podać listy zwracane przez loadfile i tytuł wykresu (nazwa pliku/użyte parametry)
def hist(allIn, illIn, infectedOut, allOut, mask, title):
    plt.suptitle(title)
    plt.subplots_adjust(left=0.1, bottom=0.1, right=0.9, top=0.85, wspace=0.4, hspace=0.6)
    plt.subplot(2,2,1)
    plt.hist(allIn, align = 'left')
    plt.title('Liczba osób na wejściu')
    plt.xlabel('Liczba osób')
    plt.ylabel('Liczba symulacji')
    plt.subplot(2,2,2)
    plt.hist(allOut, align = 'left')
    plt.title('Liczba osób na wyjściu')
    plt.xlabel('Liczba osób')
    plt.ylabel('Liczba symulacji')
    plt.subplot(2,2,3)
    plt.hist(illIn, align = 'left')
    plt.title('Liczba chorych osób na wejściu')
    plt.xlabel('Liczba osób')
    plt.ylabel('Liczba symulacji')
    plt.subplot(2,2,4)
    plt.hist(infectedOut, align = 'left')
    plt.title('Liczba zarażonych osób na wyjściu')
    plt.xlabel('Liczba osób')
    plt.ylabel('Liczba symulacji')
    plt.show()
    plt.hist(mask, align = 'left')
    plt.suptitle(title)
    plt.title('Liczba osób mających maski')
    plt.xlabel('Liczba osób')
    plt.ylabel('Liczba symulacji')
    plt.show()

# rysuje histogramy dla wszystkich plików
# wymaga podania nazwy folderu z plikami i ścieżki do niego
def all_hist(data, path):
    files = os.listdir(data)
    for file in files:
        allIn, illIn, infectedOut, allOut, mask = loadfile(path + file)
        hist(allIn, illIn, infectedOut, allOut, mask, file)


# zwraca średnią i odchylenie standardowe zliczanych wartości
def statistics(allIn, illIn, infectedOut, allOut, mask):
    allIn_mean = np.mean(allIn)
    allIn_std = np.std(allIn)
    illIn_mean = np.mean(illIn)
    illIn_std = np.std(illIn)
    infectedOut_mean = np.mean(infectedOut)
    infectedOut_std = np.std(infectedOut)
    allOut_mean = np.mean(allOut)
    allOut_std = np.std(allOut)
    mask_mean = np.mean(mask)
    mask_std = np.std(mask)
    # print("Zdrowe osoby na wejściu: średnia: {} odchylenie: {}".format(str(allIn_mean), str(allIn_std)))
    # print("Chore osoby na wejściu: średnia: {} odchylenie: {}".format(str(illIn_mean), str(illIn_std)))
    # print("Zarażone osoby na wyjściu: średnia: {} odchylenie: {}".format(str(infectedOut_mean), str(infectedOut_std)))
    # print("Chore osoby na wyjściu: średnia: {} odchylenie: {}".format(str(allOut_mean), str(allOut_std)))
    # print("Osoby noszące maski: średnia: {} odchylenie: {}".format(str(mask_mean), str(mask_std)))
    return allIn_mean, allIn_std, illIn_mean, illIn_std, infectedOut_mean, infectedOut_std, allOut_mean, allOut_std, mask_mean, mask_std



# rysuje wykres zmian średnich wartości w zależności od zmiany parametrów
# wymaga podania listy plików i wartości zmiennego parametru
def parameter(files, param, title, path):
    mean_allIn_all = []
    mean_illIn_all = []
    mean_infectedOut_all = []
    mean_allOut_all = []
    mean_mask_all = []
    std_allIn_all = []
    std_illIn_all = []
    std_infectedOut_all = []
    std_allOut_all = []
    std_mask_all = []
    for file in files:
        allIn, illIn, infectedOut, allOut, mask = loadfile(path+file)
        allIn_mean, allIn_std, illIn_mean, illIn_std, infectedOut_mean, infectedOut_std, allOut_mean, allOut_std, mask_mean, mask_std = statistics(allIn, illIn, infectedOut, allOut, mask)
        mean_allIn_all.append(allIn_mean)
        mean_illIn_all.append(illIn_mean)
        mean_infectedOut_all.append(infectedOut_mean)
        mean_allOut_all.append(allOut_mean)
        mean_mask_all.append(mask_mean)
        std_allIn_all.append(allIn_std)
        std_illIn_all.append(illIn_std)
        std_infectedOut_all.append(infectedOut_std)
        std_allOut_all.append(allOut_std)
        std_mask_all.append(mask_std)

    plt.errorbar(param,mean_allIn_all, yerr = std_allIn_all, fmt = '.')
    plt.suptitle(title)
    plt.xlabel('Wartość parametru')
    plt.ylabel('Średnia liczba osób')
    plt.title('Liczba osób na wejściu')
    plt.show()
    plt.errorbar(param,mean_illIn_all, yerr = std_illIn_all, fmt = '.')
    plt.suptitle(title)
    plt.xlabel('Wartość parametru')
    plt.ylabel('Średnia liczba osób')
    plt.title('Liczba osób chorych na wejściu')
    plt.show()
    plt.errorbar(param,mean_infectedOut_all, yerr = std_infectedOut_all, fmt = '.')
    plt.suptitle(title)
    plt.xlabel('Wartość parametru')
    plt.ylabel('Średnia liczba osób')
    plt.title('LIczba osób zarażonych na wyjściu')
    plt.show()
    plt.errorbar(param,mean_allOut_all, yerr = std_allOut_all, fmt = '.')
    plt.suptitle(title)
    plt.xlabel('Wartość parametru')
    plt.ylabel('Średnia liczba osób')
    plt.title('Liczba osób na wyjściu')
    plt.show()
    plt.errorbar(param,mean_mask_all, yerr = std_mask_all, fmt = '.')
    plt.suptitle(title)
    plt.xlabel('Wartość parametru')
    plt.ylabel('Średnia liczba osób')
    plt.title('Liczba osób noszących maseczki')
    plt.show()


prob_in = ['1.0','10.0', '20.0', '30.0', '40.0', '50.0', '60.0', '70.0']
virus_death = ['1.0', '20.0', '50.0']
mask = ['10.0', '30.0', '50.0', '70.0', '80.0', '90.0', '100.0']
status_I = ['1.0', '10.0', '15.0', '20.0', '30.0', '40.0', '50.0']
virus_trans = ['1.0', '10.0',  '30.0', '50.0']
prob_I = ['0.05', '0.5', '0.7']


# rysuje wykresy średniej liczby osób w zależności od parametru dla wszystkich parametrów w danym pomieszczeniu
# wymaga podania folderu z plikami i ścieżki do niego
def all_plots(data, path):
    list_of_files = os.listdir(data)
    parameters = []
    for file in list_of_files:
        f = file.replace('.txt', '')
        f = f.split(',')
        parameters.append(f)
    files_prob_in = []
    files_mask = []
    files_virus_death = []
    files_status_I = []
    files_virus_trans = []
    files_prob_I = []

    for i in range(len(parameters)):
        if parameters[i][2] in prob_in:
            files_prob_in.append(list_of_files[i])
        elif parameters[i][4] in mask:
            files_mask.append(list_of_files[i])
        elif parameters[i][6] in virus_death:
            files_virus_death.append(list_of_files[i])
        elif parameters[i][7] in virus_trans:
            files_virus_trans.append(list_of_files[i])
        elif parameters[i][8] in status_I:
            files_status_I.append(list_of_files[i])
        elif parameters[i][10] in prob_I:
            files_prob_I.append(list_of_files[i])

    files_prob_in.sort()
    files_status_I.sort()
    files_virus_trans.sort()
    files_virus_death.sort()
    files_mask.sort()
    files_prob_I.sort()


    parameter(files_prob_I, prob_I, "Zmieniane prawdopodobieństwo zarażenia", path)
    parameter(files_mask, mask, "Zmieniane prawdopodobieństwo posiadania maseczki", path)
    parameter(files_virus_death, virus_death,'Zmieniany procent umieralności wirusa w każdym kroku', path)
    parameter(files_virus_trans, virus_trans, 'Zmieniany procent wirusa przekazywany na sąsiednie pola', path)
    parameter(files_status_I, status_I, 'Zmieniane prawdopodobieństwo, że osoba wchodząca jest zarażona', path)
    parameter(files_prob_in, prob_in, 'Zmieniane prawdopodobieństwo wejścia nowego człowieka', path)

#all_hist('gym_DANE', 'gym_DANE/')
all_plots('gym_DANE', 'gym_DANE/')
