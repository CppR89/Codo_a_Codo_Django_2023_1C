# %%
# --------------------------------------------------------------------
# -- Import --#
# --------------------------------------------------------------------
from Persona import Persona
from Cuenta import Cuenta
# --------------------------------------------------------------------
# -- Fin Import --#
# --------------------------------------------------------------------

# --------------------------------------------------------------------
# -- Definicion de la clase --#
# --------------------------------------------------------------------
class CuentaJoven(Cuenta):
    def __init__(self, titular, cantidad, bonificacion):
        #Aqui pones como van los atributos de la clase madre
        super().__init__(titular, cantidad)
        self.bonificacion = bonificacion
    
    # --------------------------------------------------------------------
    # -- Getters & Setter --#
    # --------------------------------------------------------------------
    @property
    #getter
    def bonificacion(self):
        return self._bonificacion
    #--------------------------------------------------------------------
    @bonificacion.setter
    #setter
    def bonificacion(self, bonificacion):
        if isinstance(bonificacion, float) and bonificacion >= 0:
            self._bonificacion = bonificacion
        else:
            raise ValueError("Valor erroneo")
    # --------------------------------------------------------------------
    # -- Fin Getters & Setter --#
    # --------------------------------------------------------------------
    
    # --------------------------------------------------------------------
    # -- Metodos comunes --#
    # --------------------------------------------------------------------
    #--------------------------------------------------------------------
    # --------------------------------------------------------------------
    # -- Metodo redefinido --#
    # --------------------------------------------------------------------
    def retirar(self, cantidad):
        if self.es_titular_valido(): #Aqui no pongas self.
            self.cantidad -= cantidad
        else:
            print("No es titular valido")
    # --------------------------------------------------------------------
    # -- Fin Metodo redefinido --#
    # --------------------------------------------------------------------
    #--------------------------------------------------------------------
    # --------------------------------------------------------------------
    # -- Metodo propio de la clase --#
    # --------------------------------------------------------------------
    def es_titular_valido(self):
        if self.titular.edad >= 18 and self.titular.edad <=25:
            return True
        else:
            return False
    # --------------------------------------------------------------------
    # -- Fin Metodo propio de la clase --#
    # --------------------------------------------------------------------
    #--------------------------------------------------------------------
    # --------------------------------------------------------------------
    # -- Fin Metodos comunes --#
    # --------------------------------------------------------------------
# --------------------------------------------------------------------
# -- Fin Definicion de la clase --#
# --------------------------------------------------------------------
"""------------------------------------------------------------------------------------------------------------
S E P A R A D O R  -  S E P A R A D O R  -  S E P A R A D O R  -  S E P A R A D O R  -  S E P A R A D O R
------------------------------------------------------------------------------------------------------------"""
# %% [markdown]
# # Creo las personas
# ## Retroceder Nunca, Rendirse Jamas..
# **Personas**
persona1 = Persona("Juan",39,"536464")
persona2 = Persona("Jorgito",20,"32168")
# %% [markdown]
# # Creo las cuentas jovenes
# ## Retroceder Nunca, Rendirse Jamas..
# **Cuentas jovenes**
cuentajoven1 = CuentaJoven(persona1, 10000.0, 15.0)
cuentajoven2 = CuentaJoven(persona2, 10000.0, 15.0)
#--------------------------------------------------------------------
# %%
