import streamlit as st

# ---------- BASIC PAGE CONFIG ----------
st.set_page_config(
    page_title="Poszukiwacze skarbów – alokacja dóbr",
    layout="wide"
)

# ---------- UTILITY FUNCTIONS (NIEWIDOCZNE DLA UCZNIÓW) ----------
def u_IJ(x1, x2, x3):
    # Indiana Jones: u_IJ(x) = min{2x1, x2, 2x3}
    return min(2 * x1, x2, 2 * x3)

def u_LC(x1, x2, x3):
    # Lara Croft: u_LC(x) = min{x1, x2, 2x3}
    return min(x1, x2, 2 * x3)

def u_ND(x1, x2, x3):
    # Nathan Drake: u_ND(x) = min{2x1, 2x2, x3}
    return min(2 * x1, 2 * x2, x3)

def generate_feasible_allocations():
    """
    Generuje wszystkie dopuszczalne alokacje:
    - 4 liny
    - 5 pistoletów
    - 5 lornetek
    między 3 osoby (IJ, LC, ND).
    Zwraca listę trójek:
    ((IJ_l, LC_l, ND_l), (IJ_p, LC_p, ND_p), (IJ_lo, LC_lo, ND_lo))
    """
    allocations = []

    # Liny: suma = 4
    for IJ_l in range(5):
        for LC_l in range(5 - IJ_l):
            ND_l = 4 - IJ_l - LC_l
            if ND_l < 0 or ND_l > 4:
                continue

            # Pistolety: suma = 5
            for IJ_p in range(6):
                for LC_p in range(6 - IJ_p):
                    ND_p = 5 - IJ_p - LC_p
                    if ND_p < 0 or ND_p > 5:
                        continue

                    # Lornetki: suma = 5
                    for IJ_lo in range(6):
                        for LC_lo in range(6 - IJ_lo):
                            ND_lo = 5 - IJ_lo - LC_lo
                            if ND_lo < 0 or ND_lo > 5:
                                continue

                            allocations.append(
                                ((IJ_l, LC_l, ND_l),
                                 (IJ_p, LC_p, ND_p),
                                 (IJ_lo, LC_lo, ND_lo))
                            )
    return allocations

def improvement_possible_for(hero_index, current_utils, allocations):
    """
    Sprawdza, czy istnieje inna dopuszczalna alokacja,
    w której:
    - bohater hero_index ma *wyższą* użyteczność,
    - a pozostali nie mają niższej użyteczności
      niż w current_utils.
    hero_index: 0 = Indiana, 1 = Lara, 2 = Nathan
    """
    for alloc in allocations:
        (l_liny, p_pisty, b_lorn) = alloc

        IJ_liny, LC_liny, ND_liny = l_liny
        IJ_pisty, LC_pisty, ND_pisty = p_pisty
        IJ_lornetki, LC_lornetki, ND_lornetki = b_lorn

        u_IJ_new = u_IJ(IJ_liny, IJ_pisty, IJ_lornetki)
        u_LC_new = u_LC(LC_liny, LC_pisty, LC_lornetki)
        u_ND_new = u_ND(ND_liny, ND_pisty, ND_lornetki)

        utils_new = (u_IJ_new, u_LC_new, u_ND_new)

        # Bohater musi mieć lepiej
        if utils_new[hero_index] <= current_utils[hero_index]:
            continue

        # Pozostali nie mogą mieć gorzej
        others_ok = True
        for j in range(3):
            if j == hero_index:
                continue
            if utils_new[j] < current_utils[j]:
                others_ok = False
                break

        if others_ok:
            return True

    return False


# Prekomputujemy wszystkie dopuszczalne alokacje
ALL_ALLOCATIONS = generate_feasible_allocations()

# ---------- OPIS ZADANIA DLA UCZNIÓW ----------
st.title("Poszukiwacze skarbów – podział lin, pistoletów i lornetek")

st.markdown(
"""
Mamy trzech poszukiwaczy skarbów:

- **Indiana Jones (IJ)**  
- **Lara Croft (LC)**  
- **Nathan Drake (ND)**  

Każdy potrzebuje trzech rodzajów sprzętu:

1. lin magnetycznych do wspinaczki  
2. pistoletów  
3. lornetek z noktowizorem  

Każda postać ma **inne priorytety**:

- **Larze** najbardziej zależy na **linach i pistoletach**,  
- **Indianie** najbardziej zależy na **pistoletach**,  
- **Nathanowi** najbardziej zależy na **lornetkach**.

Początkowa alokacja dóbr (w kolejności: liny, pistolety, lornetki) jest następująca:

- Indiana Jones: **(1, 0, 3)**  
- Lara Croft: **(0, 4, 0)**  
- Nathan Drake: **(3, 1, 1)**  

Łączne zasoby dostępne w grupie:

- liny: **4**  
- pistolety: **5**  
- lornetki: **5**

**Twoje zadanie:**

Zaproponuj własny podział tych zasobów (tak, aby sumy się zgadzały),  
a następnie sprawdź, jak bardzo „zadowolony” będzie każdy poszukiwacz.
"""
)

st.markdown("---")

# ---------- OBRAZKI I POLA WEJŚCIOWE (ORYGINALNY ROZMIAR OBRAZÓW) ----------
col_IJ, col_LC, col_ND = st.columns([1, 1, 1])

with col_IJ:
    st.subheader("Indiana Jones (IJ)")
    try:
        st.image("indiana.png", use_column_width=False)   # oryginalny rozmiar
    except Exception:
        st.info("Brak pliku **indiana.png** w katalogu aplikacji.")

    st.markdown("**Podział dóbr dla Indiany**")
    IJ_liny = st.number_input("Liny (IJ)", min_value=0, max_value=4, value=1, step=1)
    IJ_pisty = st.number_input("Pistolety (IJ)", min_value=0, max_value=5, value=0, step=1)
    IJ_lornetki = st.number_input("Lornetki (IJ)", min_value=0, max_value=5, value=3, step=1)

with col_LC:
    st.subheader("Lara Croft (LC)")
    try:
        st.image("lara.png", use_column_width=False)
    except Exception:
        st.info("Brak pliku **lara.png** w katalogu aplikacji.")

    st.markdown("**Podział dóbr dla Lary**")
    LC_liny = st.number_input("Liny (LC)", min_value=0, max_value=4, value=0, step=1)
    LC_pisty = st.number_input("Pistolety (LC)", min_value=0, max_value=5, value=4, step=1)
    LC_lornetki = st.number_input("Lornetki (LC)", min_value=0, max_value=5, value=0, step=1)

with col_ND:
    st.subheader("Nathan Drake (ND)")
    try:
        st.image("nathan.png", use_column_width=False)
    except Exception:
        st.info("Brak pliku **nathan.png** w katalogu aplikacji.")

    st.markdown("**Podział dóbr dla Nathana**")
    ND_liny = st.number_input("Liny (ND)", min_value=0, max_value=4, value=3, step=1)
    ND_pisty = st.number_input("Pistolety (ND)", min_value=0, max_value=5, value=1, step=1)
    ND_lornetki = st.number_input("Lornetki (ND)", min_value=0, max_value=5, value=1, step=1)

st.markdown("---")

# ---------- SPRAWDZENIE SUM ZASOBÓW ----------
sum_liny = IJ_liny + LC_liny + ND_liny
sum_pisty = IJ_pisty + LC_pisty + ND_pisty
sum_lornetki = IJ_lornetki + LC_lornetki + ND_lornetki

st.subheader("Sprawdzenie, czy podział jest dopuszczalny")

cols_check = st.columns(3)
with cols_check[0]:
    if sum_liny == 4:
        st.success(f"Liny: {sum_liny} / 4 – OK")
    else:
        st.error(f"Liny: {sum_liny} / 4 – suma musi być równa 4")

with cols_check[1]:
    if sum_pisty == 5:
        st.success(f"Pistolety: {sum_pisty} / 5 – OK")
    else:
        st.error(f"Pistolety: {sum_pisty} / 5 – suma musi być równa 5")

with cols_check[2]:
    if sum_lornetki == 5:
        st.success(f"Lornetki: {sum_lornetki} / 5 – OK")
    else:
        st.error(f"Lornetki: {sum_lornetki} / 5 – suma musi być równa 5")

st.markdown("---")

# ---------- LICZENIE UŻYTECZNOŚCI / ZADOWOLENIA ----------
if st.button("Policz poziom zadowolenia bohaterów"):
    # Bieżące użyteczności
    u_IJ_now = u_IJ(IJ_liny, IJ_pisty, IJ_lornetki)
    u_LC_now = u_LC(LC_liny, LC_pisty, LC_lornetki)
    u_ND_now = u_ND(ND_liny, ND_pisty, ND_lornetki)
    utils_now = (u_IJ_now, u_LC_now, u_ND_now)

    st.subheader("Poziomy zadowolenia (użyteczności)")

    col_u1, col_u2, col_u3 = st.columns(3)
    col_u1.metric("Indiana", u_IJ_now)
    col_u2.metric("Lara", u_LC_now)
    col_u3.metric("Nathan", u_ND_now)

    st.markdown("---")
    st.subheader("Zadania: czy można jeszcze kogoś „poprawić”?")

    # Indiana
    if improvement_possible_for(0, utils_now, ALL_ALLOCATIONS):
        st.info(
            "Spróbuj **zwiększyć użyteczność (zadowolenie) Indiany**, "
            "nie zmniejszając przy tym użyteczności **Lary ani Nathana** – "
            "to wciąż jest możliwe dla jakiegoś innego podziału."
        )
    else:
        st.success(
            "Nie można już bardziej zwiększyć użyteczności **Indiany**, "
            "nie zmniejszając przy tym użyteczności **Lary ani Nathana**."
        )

    # Lara
    if improvement_possible_for(1, utils_now, ALL_ALLOCATIONS):
        st.info(
            "Spróbuj **zwiększyć użyteczność Lary**, "
            "nie zmniejszając przy tym użyteczności **Indiany ani Nathana** – "
            "to wciąż jest możliwe dla jakiegoś innego podziału."
        )
    else:
        st.success(
            "Nie można już bardziej zwiększyć użyteczności **Lary**, "
            "nie zmniejszając przy tym użyteczności **Indiany ani Nathana**."
        )

    # Nathan
    if improvement_possible_for(2, utils_now, ALL_ALLOCATIONS):
        st.info(
            "Spróbuj **zwiększyć użyteczność Nathana**, "
            "nie zmniejszając przy tym użyteczności **Indiany ani Lary** – "
            "to wciąż jest możliwe dla jakiegoś innego podziału."
        )
    else:
        st.success(
            "Nie można już bardziej zwiększyć użyteczności **Nathana**, "
            "nie zmniejszając przy tym użyteczności **Indiany ani Lary**."
        )

    # ---------- PORÓWNANIE Z ALOKACJĄ POCZĄTKOWĄ (DLA CIEKAWYCH) ----------
    u_IJ_init = u_IJ(1, 0, 3)
    u_LC_init = u_LC(0, 4, 0)
    u_ND_init = u_ND(3, 1, 1)

    with st.expander("Porównanie z alokacją początkową"):
        st.markdown(
            f"""
            **Alokacja początkowa:**  
            - Indiana: użyteczność **{u_IJ_init}**  
            - Lara: użyteczność **{u_LC_init}**  
            - Nathan: użyteczność **{u_ND_init}**  

            **Twoja alokacja:**  
            - Indiana: **{u_IJ_now}**  
            - Lara: **{u_LC_now}**  
            - Nathan: **{u_ND_now}**
            """
        )