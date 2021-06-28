# MODELOWANIE EPIDEMIOLOGICZNE
> Celem projektu było stworzenie projektu, który pozwala zasymulować rozprzestrzenianie się wirusa w zależności od przemieszczania się ludzi w pomieszczeniu.
## SPIS TREŚCI
* WPROWADZENIE
* UŻYTE TECHNOLOGIE
* URUCHOMIENIE
* PRZYKŁAD UŻYCIA
* STATUS PROJEKTU
## WPROWADZENIE
>Na podstawie podanych parametrów program przeprowadza symulację przemieszczania się ludzi w zamkniętym pomieszczeniu oraz ich zarażania. Czym większe stężenie
>wirusa w miejscu pobytu człowieka tym większa szansa na jego zarażenie. Projekt zakłada trzy stany człowieka: S (zdrowy), I (zarażony) oraz SI (zarażony w pomieszczeniu).
## UŻYTE TECHNOLOGIE
- Python
## URUCHOMIENIE
main.py space paths steps prob_in mask max_humans status_I virus virus_death virus_trans prob_I max_prob_I factor_mask

* space - plik tekstowy z wymiarami obiektu
* paths - plik tekstowy ze ścieżkami
* steps - int, liczba cykli symulacji
* prob_in - float, prawdopodobieństwo w % pojawienia się nowego człowieka
* mask - float, prawdopodobieństwo w % posiadania maseczki
* max_humans - maksymalna liczba ludzi znajdujących się w jednostce przestrzeni
* status_I - float, prawdopodobieństwo w %, że osoba, która wchodzi jest zarażona
* virus - float, ilość pozostawianego wirusa przez osobę zarażoną
* virus_death - float, jaki procent wirusa umiera w każdym kroku
* virus_trans - float, jaki procent wirusa jest przekazywany na sąsiednie pola
* prob_I - float, prawdopodobieńśtwo w % zarażenia przez jednostkę wirusa
* max_prob_I - float, maksymalne prawdopodobieństwo w % zarażenia
* factor_mask - float, ile razy zmniejsza się prawdopodobieństwo zarażenia w maseczce
>PLIK SPACE: w osobnych liniach podaje się: nazwę identyfikacyjną, a po spacji jej współrzędne (x i y rozdzielone przecinkiem)
>również rozdzielone spacją,
>możliwe nazwy do użycia to: object (współrzędne wierzchołków obiektu), door (współrzędne drzwi zewnętrzych),
>size (rozmiar macierzy symulacji - współrzędne object powinny mieścić się w size), 
>active (współrzędne pola na którym może stanąć człowiek), cashdesk (współrzędne kasy lub recepcji, poprzedzone parametrem 'above'/ 'below', w zależności od tego, z której strony podchodzą ludzie- będzie tam występować kolejka), excluded (współrzędne miejsc na któych nie może stanąć człowiek),
>inwalls (współrzędne ścian znajdujących się w object), indoors (współrzędne drzwi znajdujących się w object)
>
>PLIK PATHS: każdy przejście jest zapisywane w trzech liniach: w pierwszej - współrzędne wierzchołka; w drugiej - współrzędne wierzchołków na które możemy przejść z podanego wyżej,
>w trzeciej - prawdopodobieństwo * 100 przejścia na dany wierzchołek. Współrzędne x i y rozdzielone są przecinkiem, a reszta spacjami.
>Przykładowe pliki: space (gym.txt, tramwaj.txt, sklep_zespolowe.txt), paths (gym_path.txt, tram_path.txt, sklep_graf.txt) znajdują się w folderze z projektem.
## PRZYKŁAD UŻYCIA
main.py gym.txt gym_path.txt 500 10 90 3 10 1 10 20 0.1 95 5
## STATUS
w trakcie realizacji
## AUTORZY
Aleksandra Bartnik, Aleksandra Żurko, Agnieszka Motyka, Marta Giziewska
