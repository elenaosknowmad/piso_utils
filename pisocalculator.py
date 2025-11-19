"""
Happy Hipo - Property Cost Calculator
Calculates the total cost of purchasing a property including all fees and taxes.
"""

import streamlit as st
import pandas as pd

def calculate_property_costs(property_price, commission_percentage, down_payment):
    """
    Calculate all costs associated with purchasing a property.
    
    Args:
        property_price: Base price of the property
        commission_percentage: Real estate commission percentage
        down_payment: Initial down payment amount
    
    Returns:
        dict: Breakdown of all costs
    """
    # Real estate commission with VAT
    commission_base = property_price * (commission_percentage / 100)
    commission_vat = commission_base * 0.21
    commission_total = commission_base + commission_vat
    
    # ITP (Transfer tax)
    itp = property_price * 0.054
    
    # Fixed costs (appraisal + notary)
    fixed_costs = 2500
    
    # Total cost
    total_cost = property_price + commission_total + itp + fixed_costs
    
    # Additional costs (everything except property price)
    additional_costs = commission_total + itp + fixed_costs
    
    # Total needed (property + all costs)
    total_needed = total_cost
    
    # Money needed after down payment
    money_after_down_payment = total_needed - down_payment
    
    # Mortgage percentage over property price
    mortgage_percentage = (money_after_down_payment / property_price) * 100
    
    return {
        'property_price': property_price,
        'commission_base': commission_base,
        'commission_vat': commission_vat,
        'commission_total': commission_total,
        'itp': itp,
        'fixed_costs': fixed_costs,
        'additional_costs': additional_costs,
        'total_cost': total_cost,
        'down_payment': down_payment,
        'money_after_down_payment': money_after_down_payment,
        'mortgage_percentage': mortgage_percentage
    }

def format_currency(amount):
    """Format number as currency."""
    return f"{amount:,.2f} €"

def calculate_monthly_payment(loan_amount, annual_rate, years):
    """
    Calculate monthly mortgage payment using standard amortization formula.
    
    Args:
        loan_amount: Total amount to finance
        annual_rate: Annual interest rate (as percentage, e.g., 2.5 for 2.5%)
        years: Loan term in years
    
    Returns:
        float: Monthly payment amount
    """
    if loan_amount <= 0 or annual_rate <= 0 or years <= 0:
        return 0
    
    monthly_rate = (annual_rate / 100) / 12
    num_payments = years * 12
    
    # Amortization formula
    monthly_payment = loan_amount * (monthly_rate * (1 + monthly_rate)**num_payments) / ((1 + monthly_rate)**num_payments - 1)
    
    return monthly_payment

def calculate_financing_scenarios(property_price, additional_costs):
    """
    Calculate down payment needed for different financing percentages.
    
    Args:
        property_price: Base price of the property
        additional_costs: Additional costs (commission, ITP, fixed costs)
    
    Returns:
        DataFrame: Scenarios for different financing percentages
    """
    scenarios = []
    percentages = [95, 90, 85, 80]
    
    for pct in percentages:
        mortgage_amount = property_price * (pct / 100)
        down_payment_needed = property_price + additional_costs - mortgage_amount
        
        scenarios.append({
            'Financiación': f'{pct}%',
            'Hipoteca': format_currency(mortgage_amount),
            'Entrada Necesaria': format_currency(down_payment_needed)
        })
    
    return pd.DataFrame(scenarios)

def main():
    # Page configuration
    st.set_page_config(
        page_title="Happy Hipo 🦛",
        page_icon="🦛",
        layout="centered"
    )
    
    # Custom CSS for minimalist design
    st.markdown("""
        <style>
        .main {
            padding-top: 1rem;
        }
        .stApp {
            max-width: 700px;
            margin: 0 auto;
        }
        h1 {
            color: #2c3e50;
            font-weight: 300;
            font-size: 1.8rem;
            margin-bottom: 1rem;
        }
        h3 {
            font-size: 1.1rem;
            font-weight: 500;
            margin: 1rem 0 0.5rem 0;
        }
        .metric-container {
            background-color: #f8f9fa;
            padding: 1rem;
            border-radius: 6px;
            margin: 0.5rem 0;
            border-left: 3px solid #3498db;
        }
        .total-container {
            background-color: #2c3e50;
            color: white;
            padding: 1.2rem;
            border-radius: 6px;
            margin: 1rem 0;
            text-align: center;
        }
        .mortgage-container {
            background-color: #27ae60;
            color: white;
            padding: 1rem;
            border-radius: 6px;
            margin: 0.5rem 0;
            text-align: center;
        }
        .stButton>button {
            width: 100%;
            background-color: #3498db;
            color: white;
            border: none;
            padding: 0.6rem;
            border-radius: 6px;
            font-size: 0.95rem;
            font-weight: 500;
        }
        .stButton>button:hover {
            background-color: #2980b9;
        }
        [data-testid="stMetricValue"] {
            font-size: 1.1rem;
        }
        [data-testid="stMetricLabel"] {
            font-size: 0.85rem;
        }
        </style>
    """, unsafe_allow_html=True)
    
    # Header
    st.title("🦛 Happy Hipo")
    st.caption("Tu calculadora amiga para comprar casa sin sustos 🏡✨")
    
    # Input section
    col1, col2, col3 = st.columns(3)
    
    with col1:
        property_price = st.number_input(
            "Precio del Piso (€)",
            min_value=0.0,
            value=200000.0,
            step=1000.0,
            format="%.0f",
            help="Precio base de la propiedad"
        )
    
    with col2:
        commission_percentage = st.number_input(
            "Comisión (%)",
            min_value=0.0,
            max_value=100.0,
            value=3.5,
            step=0.1,
            format="%.1f",
            help="Porcentaje de comisión inmobiliaria"
        )
    
    with col3:
        down_payment = st.number_input(
            "Entrada (€)",
            min_value=0.0,
            value=42000.0,
            step=1000.0,
            format="%.0f",
            help="Cantidad de entrada que aportas"
        )
    
    st.markdown("")
    
    # Initialize session state for results
    if 'results' not in st.session_state:
        st.session_state.results = None
    
    # Calculate button
    if st.button("🦛 Calcular con Happy Hipo"):
        if property_price > 0:
            st.session_state.results = calculate_property_costs(property_price, commission_percentage, down_payment)
        else:
            st.warning("⚠️ Por favor, introduce un precio válido para el piso.")
    
    # Display results if they exist
    if st.session_state.results is not None:
        results = st.session_state.results
        
        # Create tabs
        tab1, tab2, tab3 = st.tabs(["💰 Costes Totales", "🏦 Escenarios de Financiación", "📅 Cuota Mensual"])
        
        # TAB 1: Total Costs
        with tab1:
            st.markdown("### 📊 Desglose de Costes")
            
            # Property price
            st.markdown(f"""
                <div class="metric-container">
                    <h4 style="margin: 0; color: #7f8c8d; font-size: 0.9rem;">Precio del Piso</h4>
                    <h2 style="margin: 0.3rem 0 0 0; color: #2c3e50; font-size: 1.5rem;">{format_currency(results['property_price'])}</h2>
                </div>
            """, unsafe_allow_html=True)
            
            # Commission breakdown
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Comisión Base", format_currency(results['commission_base']))
            with col2:
                st.metric("IVA (21%)", format_currency(results['commission_vat']))
            with col3:
                st.metric("Total Comisión", format_currency(results['commission_total']))
            
            # Other costs
            col1, col2 = st.columns(2)
            with col1:
                st.metric("ITP (5.4%)", format_currency(results['itp']))
            with col2:
                st.metric("Tasación + Notaría", format_currency(results['fixed_costs']))
            
            # Total cost (highlighted)
            st.markdown(f"""
                <div class="total-container">
                    <h3 style="margin: 0; font-weight: 300; font-size: 0.95rem;">COSTE TOTAL</h3>
                    <h1 style="margin: 0.5rem 0 0 0; font-size: 2rem; font-weight: 300;">{format_currency(results['total_cost'])}</h1>
                </div>
            """, unsafe_allow_html=True)
            
            # Additional costs info
            st.info(f"💰 **Costes adicionales al precio del piso:** {format_currency(results['additional_costs'])} ({(results['additional_costs']/results['property_price']*100):.2f}%)")
        
        # TAB 2: Financing Scenarios
        with tab2:
            st.markdown("### 🏦 Tu Financiación Actual")
            
            col1, col2 = st.columns(2)
            with col1:
                st.metric("Entrada Aportada", format_currency(results['down_payment']))
            with col2:
                st.metric("Cantidad a Financiar", format_currency(results['money_after_down_payment']))
            
            # Mortgage percentage
            st.markdown(f"""
                <div class="mortgage-container">
                    <h4 style="margin: 0; font-weight: 300; font-size: 0.9rem;">PORCENTAJE DE HIPOTECA</h4>
                    <h2 style="margin: 0.3rem 0 0 0; font-size: 1.8rem; font-weight: 400;">{results['mortgage_percentage']:.1f}%</h2>
                    <p style="margin: 0.3rem 0 0 0; font-size: 0.85rem; opacity: 0.9;">sobre el precio del piso</p>
                </div>
            """, unsafe_allow_html=True)
            
            if results['mortgage_percentage'] > 80:
                st.warning("⚠️ La mayoría de bancos no conceden hipotecas superiores al 80% del valor del inmueble.")
            elif results['mortgage_percentage'] > 70:
                st.info("ℹ️ El porcentaje de hipoteca está entre el 70-80%. Algunas entidades pueden requerir condiciones adicionales.")
            else:
                st.success("✅ El porcentaje de hipoteca es favorable (≤70%).")
            
            st.markdown("")
            st.markdown("### 📋 Escenarios de Financiación")
            st.caption("¿Cuánto necesitas de entrada según el % de hipoteca?")
            
            # Generate financing scenarios
            scenarios_df = calculate_financing_scenarios(results['property_price'], results['additional_costs'])
            
            # Display table with custom styling
            st.dataframe(
                scenarios_df,
                hide_index=True,
                width='stretch'
            )
            
            st.info("💡 **Recuerda:** La entrada debe cubrir los gastos adicionales + la diferencia entre el precio y la hipoteca.")
        
        # TAB 3: Monthly Payment
        with tab3:
            st.markdown("### 📅 Calcula tu Cuota Mensual")
            
            # Initialize session state for mortgage parameters
            if 'interest_rate' not in st.session_state:
                st.session_state.interest_rate = 2.5
            if 'loan_years' not in st.session_state:
                st.session_state.loan_years = 30
            
            col1, col2 = st.columns(2)
            with col1:
                interest_rate = st.number_input(
                    "TAE (%) 📈",
                    min_value=0.0,
                    max_value=15.0,
                    value=st.session_state.interest_rate,
                    step=0.1,
                    format="%.2f",
                    help="Tipo de interés anual",
                    key="interest_rate_input"
                )
                st.session_state.interest_rate = interest_rate
            with col2:
                loan_years = st.number_input(
                    "Años 📆",
                    min_value=5,
                    max_value=40,
                    value=st.session_state.loan_years,
                    step=1,
                    help="Plazo de la hipoteca en años",
                    key="loan_years_input"
                )
                st.session_state.loan_years = loan_years
            
            # Calculate monthly payment
            monthly_payment = calculate_monthly_payment(
                results['money_after_down_payment'],
                interest_rate,
                loan_years
            )
            
            # Display monthly payment
            st.markdown(f"""
                <div class="total-container">
                    <h3 style="margin: 0; font-weight: 300; font-size: 0.95rem;">CUOTA MENSUAL</h3>
                    <h1 style="margin: 0.5rem 0 0 0; font-size: 2rem; font-weight: 300;">{format_currency(monthly_payment)}</h1>
                    <p style="margin: 0.5rem 0 0 0; font-size: 0.85rem; opacity: 0.8;">durante {loan_years} años</p>
                </div>
            """, unsafe_allow_html=True)
            
            # Additional information
            total_to_pay = monthly_payment * loan_years * 12
            total_interest = total_to_pay - results['money_after_down_payment']
            
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Total a Pagar", format_currency(total_to_pay))
            with col2:
                st.metric("Intereses Totales", format_currency(total_interest))
            with col3:
                st.metric("Nº de Cuotas", f"{loan_years * 12}")
            
            # Income recommendation
            recommended_income = monthly_payment / 0.35
            st.info(f"💡 **Ingresos recomendados:** {format_currency(recommended_income)}/mes (la cuota no debería superar el 35% de tus ingresos)")
    
    # Footer
    st.markdown("")
    st.markdown("""
        <div style="text-align: center; color: #7f8c8d; font-size: 0.8rem; padding-top: 1rem; border-top: 1px solid #ecf0f1;">
            <p><strong>Nota:</strong> ITP del 5.4% y costes fijos de 2.500€ (tasación + notaría)</p>
            <p style="font-size: 0.75rem;">Los cálculos son aproximados y pueden variar según la ubicación y circunstancias específicas.</p>
        </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
