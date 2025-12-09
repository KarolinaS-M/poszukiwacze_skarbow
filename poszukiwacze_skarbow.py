import streamlit as st

# ---------- BASIC PAGE CONFIG ----------
st.set_page_config(
    page_title="Poszukiwacze skarbów – alokacja dóbr",
    layout="wide"
)

# ---------- UTILITY FUNCTIONS (HIDDEN FROM STUDENTS) ----------
def u_IJ(x1, x2, x3):
    # Indiana Jones: u_IJ(x) = min{2x1, x2, 2x3}
    return min(2 * x1, x2, 2 * x3)

def u_LC(x1, x2, x3):
    # Lara Croft: u_LC(x) = min{x1, x2, 2x3}
    return min(x1, x2, 2 * x3)

def u_ND(x1, x2, x3):
    # Nathan Drake: u_ND(x) = min{2x1, 2x2, x3}
    return min(2 * x1, 2 * x2, x3)


# ---------- TEXT / STORY ----------
st.title("Poszukiwacze skarbów – podział lin, pistoletów i lornetek")

st.markdown(
"""
Mamy trzech poszukiwaczy skarbów:

- **Indiana Jones (IJ)**  
- **Lara Croft (LC)**  
- **Nathan Drake (ND)**  

Każdy z nich potrzebuje trzech rzeczy:

1. lin magnetycznych do wspinaczki,  
2. pistoletów,  
3. lornetek z noktowizorem.

Początkowa alokacja dóbr jest następująca (w porządku: liny, pistolety, lornetki):

- Indiana Jones: $a_{IJ} = (1, 0, 3)$  
- Lara Croft: $a_{LC} = (0, 4, 0)$  
- Nathan Drake: $a_{ND} = (3, 1, 1)$  

Łączne zasoby na wyprawie:

- liny: **4**  
- pistolety: **5**  
- lornetki: **5**

**Pytanie:** Czy ta alokacja początkowa jest dla nich dobra?  
Spotykają się i mogą wymienić się dobrami.  
Zaproponuj nowy podział lin, pistoletów i lornetek między trójkę poszukiwaczy (tak, aby zgadzały się całkowite liczby dóbr), a następnie policz, jak na tym wychodzi każdy z nich.
"""
)

st.markdown("---")

# ---------- LAYOUT WITH IMAGES AND INPUTS ----------
col_IJ, col_LC, col_ND = st.columns(3)

# ----- Indiana -----
with col_IJ:
    st.subheader("Indiana Jones (IJ)")
    try:
        st.image("indiana.png", use_column_width=True)
    except Exception:
        st.info("Tu możesz dodać obrazek Indiany (plik **indiana.png**).")

    st.markdown("**Podział dóbr dla Indiany**")
    IJ_liny = st.number_input(
        "Liny (IJ)", min_value=0, max_value=4, value=1, step=1
    )
    IJ_pisty = st.number_input(
        "Pistolety (IJ)", min_value=0, max_value=5, value=0, step=1
    )
    IJ_lornetki = st.number_input(
        "Lornetki (IJ)", min_value=0, max_value=5, value=3, step=1
    )

# ----- Lara -----
with col_LC:
    st.subheader("Lara Croft (LC)")
    try:
        st.image("lara.png", use_column_width=True)
    except Exception:
        st.info("Tu możesz dodać obrazek Lary (plik **lara.png**).")

    st.markdown("**Podział dóbr dla Lary**")
    LC_liny = st.number_input(
        "Liny (LC)", min_value=0, max_value=4, value=0, step=1
    )
    LC_pisty = st.number_input(
        "Pistolety (LC)", min_value=0, max_value=5, value=4, step=1
    )
    LC_lornetki = st.number_input(
        "Lornetki (LC)", min_value=0, max_value=5, value=0, step=1
    )

# ----- Nathan -----
with col_ND:
    st.subheader("Nathan Drake (ND)")
    try:
        st.image("nathan.png", use_column_width=True)
    except Exception:
        st.info("Tu możesz dodać obrazek Nathana (plik **nathan.png**).")

    st.markdown("**Podział dóbr dla Nathana**")
    ND_liny = st.number_input(
        "Liny (ND)", min_value=0, max_value=4, value=3, step=1
    )
    ND_pisty = st.number_input(
        "Pistolety (ND)", min_value=0, max_value=5, value=1, step=1
    )
    ND_lornetki = st.number_input(
        "Lornetki (ND)", min_value=0, max_value=5, value=1, step=1
    )

st.markdown("---")

# ---------- CHECK FEASIBILITY ----------
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

st.markdown(
"""
Możesz zmieniać wartości tak długo, aż wszystkie trzy komunikaty będą **zielone**.  
Dopiero wtedy mamy poprawny podział zasobów.
"""
)

st.markdown("---")

# ---------- BUTTON: COMPUTE UTILITIES ----------
if st.button("Policz „zadowolenie” bohaterów dla tej alokacji"):
    # Compute utilities for the chosen allocation
    u_IJ_now = u_IJ(IJ_liny, IJ_pisty, IJ_lornetki)
    u_LC_now = u_LC(LC_liny, LC_pisty, LC_lornetki)
    u_ND_now = u_ND(ND_liny, ND_pisty, ND_lornetki)

    st.subheader("„Zadowolenie” postaci dla wybranego podziału")

    col_u1, col_u2, col_u3 = st.columns(3)
    with col_u1:
        st.metric("Indiana – poziom zadowolenia", u_IJ_now)
    with col_u2:
        st.metric("Lara – poziom zadowolenia", u_LC_now)
    with col_u3:
        st.metric("Nathan – poziom zadowolenia", u_ND_now)

    # Utilities in the initial allocation – to compare
    u_IJ_init = u_IJ(1, 0, 3)
    u_LC_init = u_LC(0, 4, 0)
    u_ND_init = u_ND(3, 1, 1)

    with st.expander("Porównanie z alokacją początkową"):
        st.markdown(
            f"""
            **Alokacja początkowa**  
            - Indiana: $a_{{IJ}} = (1, 0, 3)$, zadowolenie: **{u_IJ_init}**  
            - Lara: $a_{{LC}} = (0, 4, 0)$, zadowolenie: **{u_LC_init}**  
            - Nathan: $a_{{ND}} = (3, 1, 1)$, zadowolenie: **{u_ND_init}**  

            **Twoja alokacja**  
            - Indiana: ({IJ_liny}, {IJ_pisty}, {IJ_lornetki}) → zadowolenie: **{u_IJ_now}**  
            - Lara: ({LC_liny}, {LC_pisty}, {LC_lornetki}) → zadowolenie: **{u_LC_now}**  
            - Nathan: ({ND_liny}, {ND_pisty}, {ND_lornetki}) → zadowolenie: **{u_ND_now}**
            """
        )

        weakly_better = (
            (u_IJ_now >= u_IJ_init) and
            (u_LC_now >= u_LC_init) and
            (u_ND_now >= u_ND_init)
        )
        strictly_better_for_someone = (
            (u_IJ_now > u_IJ_init) or
            (u_LC_now > u_LC_init) or
            (u_ND_now > u_ND_init)
        )

        if weakly_better and strictly_better_for_someone:
            st.success(
                "W tej alokacji **nikt nie ma gorzej niż na początku**, "
                "a przynajmniej jedna osoba ma wyższy poziom zadowolenia."
            )
        elif (u_IJ_now == u_IJ_init) and (u_LC_now == u_LC_init) and (u_ND_now == u_ND_init):
            st.info(
                "Ta alokacja daje **dokładnie takie same** poziomy zadowolenia "
                "jak alokacja początkowa."
            )
        else:
            st.warning(
                "W tej alokacji **przynajmniej jedna osoba ma gorzej** niż w alokacji początkowej."
            )