def propagar(fosforos): 
    fosforos_quemados = fosforos.copy()
    start = 0 
    end = len(fosforos)
    for i, fosforo in enumerate(fosforos): 
        if fosforo == 1: # si el fosforo está encendido 
            mov = i 
            for j in range(mov, end): # voy para adelante 
                if fosforos_quemados[j] == -1: 
                    break 
                fosforos_quemados[j] = 1
            
            mov = i 
            for j in range(mov, start -1, -1): # voy para atras
                if fosforos_quemados[j] == -1: 
                    break 
                fosforos_quemados[j] = 1

    return fosforos_quemados 
