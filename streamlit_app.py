import streamlit as st
<<<<<<< HEAD
<<<<<<< HEAD
from clips import Environment, Symbol

<<<<<<< HEAD
st.title("🎈 Test Update Title for Lab test test")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
=======

# ---------------------------------------------------------
# Expert System (ES) – CLIPS Environment and Rules
# ---------------------------------------------------------

def create_environment():
    """
    Create and return a CLIPS Environment (Expert System engine)
    with templates and two simple rules for COVID-19 diagnosis.
    This function is called each time we want to run inference,
    which keeps the logic simple and isolated.
    """
    env = clips.Environment()

    # Define templates and rules in CLIPS language
    env.build(
        """
        ;; Template for symptoms
        (deftemplate symptom
            (slot name)
            (slot value))

        ;; Template for result diagnosis
        (deftemplate result
            (slot diagnosis))

        ;; Rule 1: If fever AND cough -> Possible COVID-19
        (defrule covid-possible
            (symptom (name fever) (value yes))
            (symptom (name cough) (value yes))
            =>
            (assert (result (diagnosis
                    "Possible COVID-19 infection. Please take a COVID-19 test and self-isolate."))))

        ;; Rule 2: If NO fever AND NO cough -> Unlikely COVID-19
        (defrule covid-unlikely
            (symptom (name fever) (value no))
            (symptom (name cough) (value no))
            =>
            (assert (result (diagnosis
                    "Unlikely to be COVID-19 based on these two symptoms."))))
        """
=======
from clips import Environment

=======
from clips import Environment

>>>>>>> f5c9ed952d2a5f7dcd464b25cc39e46a5e952e96

# ---------------------------------------------------------
# Expert System (Safe: build line-by-line)
# ---------------------------------------------------------
def create_environment():
    env = Environment()

    # --- Build templates ---
    env.build("(deftemplate symptom (slot name) (slot value))")
    env.build("(deftemplate result (slot diagnosis))")

    # --- Build rules (NO MULTILINE!!!) ---
    env.build(
        '(defrule covid-possible '
        '(symptom (name fever) (value yes)) '
        '(symptom (name cough) (value yes)) '
        '=> '
        '(assert (result (diagnosis "Possible COVID-19 infection. Please test and isolate."))))'
    )

    env.build(
        '(defrule covid-unlikely '
        '(symptom (name fever) (value no)) '
        '(symptom (name cough) (value no)) '
        '=> '
        '(assert (result (diagnosis "Unlikely COVID-19 from these symptoms."))))'
<<<<<<< HEAD
>>>>>>> f5c9ed952d2a5f7dcd464b25cc39e46a5e952e96
=======
>>>>>>> f5c9ed952d2a5f7dcd464b25cc39e46a5e952e96
    )

    return env


<<<<<<< HEAD
<<<<<<< HEAD
def run_expert_system(has_fever: bool, has_cough: bool) -> str:
    """
    Take boolean values from the User Interface (UI),
    assert them as facts into CLIPS, run inference,
    and return the diagnosis string.
    """
    env = create_environment()

    # Reset agenda and facts to initial state
    env.reset()

    # Convert booleans to 'yes' or 'no' for CLIPS
    fever_value = "yes" if has_fever else "no"
    cough_value = "yes" if has_cough else "no"

    # Assert symptom facts
    env.assert_string(f"(symptom (name fever) (value {fever_value}))")
    env.assert_string(f"(symptom (name cough) (value {cough_value}))")

    # Run inference engine
    env.run()

    # Extract result fact (if any)
    diagnosis = (
        "No specific rule was fired. Please consult a medical professional for more information."
    )
    for fact in env.facts():
        if fact.template.name == "result":
            diagnosis = fact["diagnosis"]
            break

    return diagnosis


# ---------------------------------------------------------
# Streamlit User Interface (UI)
# ---------------------------------------------------------

def main():
    st.title("🩺 COVID-19 Diagnosis Expert System (Rule-Based)")
    st.write(
        """
        This is a simple rule-based Expert System (ES) demo for COVID-19 diagnosis  
        using **clipspy (CLIPS)** and **Streamlit**.
        
        > ⚠️ **Disclaimer:** This is for educational purposes only and is **not** a medical tool.
        """
    )

    st.markdown("---")

    st.header("Step 1 – Enter Your Symptoms")

    # Radio buttons for symptoms
    fever_choice = st.radio(
        "Do you have a fever?",
        ("No", "Yes"),
        horizontal=True,
        key="fever",
    )

    cough_choice = st.radio(
        "Do you have a cough?",
        ("No", "Yes"),
        horizontal=True,
        key="cough",
    )

    # Convert to boolean values
    has_fever = fever_choice == "Yes"
    has_cough = cough_choice == "Yes"

    st.markdown("---")
    st.header("Step 2 – Run Diagnosis")

    if st.button("🧪 Diagnose"):
        diagnosis = run_expert_system(has_fever, has_cough)
        st.success(diagnosis)

        # (Optional) Show raw booleans for debugging / teaching
        with st.expander("Show internal values (for learning/debugging)", expanded=False):
            st.write(f"Fever: {has_fever}")
            st.write(f"Cough: {has_cough}")
            st.write("Rules used:")
            st.code(
                "Rule 1: IF fever == yes AND cough == yes THEN Possible COVID-19\n"
                "Rule 2: IF fever == no  AND cough == no  THEN Unlikely COVID-19",
                language="text",
            )

    st.markdown("---")
    st.caption(
        "Built for TES6313 Lab – Rule-Based Expert System using clipspy & Streamlit."
    )
=======
=======
>>>>>>> f5c9ed952d2a5f7dcd464b25cc39e46a5e952e96
# ---------------------------------------------------------
# Run Expert System
# ---------------------------------------------------------
def run_expert_system(has_fever: bool, has_cough: bool) -> str:
    env = create_environment()
    env.reset()

    fever_value = "yes" if has_fever else "no"
    cough_value = "yes" if has_cough else "no"

    env.assert_string(f"(symptom (name fever) (value {fever_value}))")
    env.assert_string(f"(symptom (name cough) (value {cough_value}))")

    env.run()

    for fact in env.facts():
        if fact.template.name == "result":
            return fact["diagnosis"]

    return "No rule fired."


# ---------------------------------------------------------
# Streamlit UI
# ---------------------------------------------------------
def main():
    st.title("🩺 COVID-19 Diagnosis Expert System (CLIPS + Streamlit)")
    st.write("Simple CLIPS rule-based diagnosis. Educational only.")

    fever = st.radio("Do you have a fever?", ["No", "Yes"], horizontal=True)
    cough = st.radio("Do you have a cough?", ["No", "Yes"], horizontal=True)

    has_fever = fever == "Yes"
    has_cough = cough == "Yes"

    if st.button("Diagnose"):
        try:
            result = run_expert_system(has_fever, has_cough)
            st.success(result)
        except Exception as e:
            st.error("CLIPS error occurred")
            st.code(str(e))
<<<<<<< HEAD
>>>>>>> f5c9ed952d2a5f7dcd464b25cc39e46a5e952e96
=======
>>>>>>> f5c9ed952d2a5f7dcd464b25cc39e46a5e952e96


if __name__ == "__main__":
    main()
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> b54ec0703cbe89e0e20c1426ed3ac927a22e2349
=======
>>>>>>> f5c9ed952d2a5f7dcd464b25cc39e46a5e952e96
=======
>>>>>>> f5c9ed952d2a5f7dcd464b25cc39e46a5e952e96
