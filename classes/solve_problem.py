from pyomo.environ import *
from classes.City import City
from itertools import chain, combinations
from typing import List

def distancia(p1, p2):
    # Função para calcular a distância euclidiana entre dois pontos (x, y)
    return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)**0.5

class OptimalSalesman:

    def __init__(self, cities : List[City]):
        self.cities = cities
        self.optimal_solution = None

    def solve(self):

        # Criando o problema de minimização
        #problem = pulp.LpProblem("Problema_Caixeiro_Viajante", pulp.LpMinimize)
        model = ConcreteModel()

        cities = [i.name for i in self.cities]

        x = Var(cities, cities, within=Binary)

        model.obj = Objective(expr=sum(i.distance_to(j) * x[i.name, j.name] 
                                       for i in self.cities for j in self.cities if i != j),
                                       sense=minimize)
        
        # Adicionando restrições:
        # 1. Cada cidade deve ser visitada exatamente uma vez
        for i in self.cities:
            model.add_constraint(sum(x[i.name, j.name] for j in self.cities if i != j) == 1)

        # 2. Não é possível ir de uma cidade para si mesma
        for i in self.cities:
            model.add_constraint(x[i.name, i.name] == 0)

        # 3. A rota deve formar um ciclo
        for i in self.cities:
            for j in self.cities:
                if i != j:
                    model.add_constraint(x[i.name, j.name] + x[j.name, i.name] <= 1)

        # Resolvendo o problema
        solver = SolverFactory("gurobi")
        solver.solve(model)

        # Restrição de subciclo
        all_subsets = self.get_subsets(self.cities)
        for s in all_subsets:
            problem += pulp.lpSum(x[(i.name, j.name)] for i in s for j in s if i != j) <= len(s) - 1

        # for cidade in cidades:
        #     for outra_cidade in cidades:
        #         if cidade != outra_cidade:
        #             problem += u[cidade.name] - u[outra_cidade.name] + len(cidades) * x[(cidade.name, outra_cidade.name)] <= len(cidades) - 1

        problem.writeLP("problema_caixeiro_viajante.lp")
        problem.solve()

        if pulp.LpStatus[problem.status] == "Optimal":
            solucao_otima = []
            for i in self.cities:
                for j in self.cities:
                    if i != j and x[(i.name, j.name)].value() == 1:
                        solucao_otima.append(i)
                        print(x[(i.name, j.name)])

            self.optimal_solution = solucao_otima
            return solucao_otima
        else:
            return None

    def get_solution_cost(self):
        if self.optimal_solution:
            return sum([self.optimal_solution[i].distance_to(self.optimal_solution[i+1]) for i in range(len(self.optimal_solution)-1)])
        else:
            return None
        
    def get_subsets(self, cities):
        s = list(cities)
        return chain.from_iterable(combinations(s, r) for r in range(1, len(s) + 1))


def problema_caixeiro_viajante(cidades : City):
    # Criando o problema de minimização
    problem = pulp.LpProblem("Problema_Caixeiro_Viajante", pulp.LpMinimize)

    # Variáveis de decisão binárias para indicar se visitamos cada cidade
    visitada = {(i, j): pulp.LpVariable(f"visitada_{i}_{j}", cat=pulp.LpBinary)
                for i in range(len(cidades)) for j in range(len(cidades))}

    # Função objetivo: minimizar a distância total percorrida
    problem += pulp.lpSum(distancia(cidades[i], cidades[j]) * visitada[(i, j)]
                         for i in range(len(cidades)) for j in range(len(cidades)))

    # Restrições
    for i in range(len(cidades)):
        # Certifique-se de que cada cidade é visitada uma única vez
        problem += pulp.lpSum(visitada[(i, j)] for j in range(len(cidades))) == 1
        problem += pulp.lpSum(visitada[(j, i)] for j in range(len(cidades))) == 1

    # Resolvendo o problema
    problem.solve()

    if pulp.LpStatus[problem.status] == "Optimal":
        # Construindo a solução ótima
        solucao_otima = []
        i, j = 0, 0
        while True:
            solucao_otima.append(cidades[i])
            for j in range(len(cidades)):
                if pulp.value(visitada[(i, j)]) == 1:
                    i = j
                    break
            if i == 0:
                break

        return solucao_otima
    else:
        return None

# # Exemplo de uso com sua lista de cidades
# cidades = [(10, 20), (15, 3), (19, 40)]
# solucao = problema_caixeiro_viajante(cidades)

# if solucao:
#     print("Solução Ótima:")
#     for i, cidade in enumerate(solucao):
#         print(f"Cidade {i + 1}: {cidade}")
# else:
#     print("Não foi possível encontrar uma solução ótima.")
