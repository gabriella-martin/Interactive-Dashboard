from streamlit_agraph import agraph, Node, Edge, Config    
        
def health_visual():
    nodes = []
    edges = []
    nodes.append( Node(id="Pandas", 
                    label="Pandas", 
                    size=15, 
                    shape="image",
                    image="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQVjjK7uT1yLWjWfIZ7dW5Bvmvs-e5DsZZPwix4SrA&s") 
                ) # includes **kwargs
    nodes.append( Node(id="Streamlit", 
                        label = 'Streamlit',
                    size=15,
                    shape="image",
                    image="https://streamlit.io/images/brand/streamlit-mark-color.svg") 
                )
    nodes.append( Node(id="Pyplot", 
                        label = 'Pyplot',
                    size=15,
                    shape="image",
                    image="https://cdn.theorg.com/39deb29f-6dae-4ac1-940c-39515deac1e5_medium.jpg") 
                )
    nodes.append( Node(id="CSV", 
                        label = 'CSV',
                    size=15,
                    shape="image",
                    image="https://cdn-icons-png.flaticon.com/512/28/28842.png") 
                )
    nodes.append( Node(id="PyiCloud", 
                        label = 'PyiCloud API',
                    size=15,
                    shape="image",
                    image="https://upload.wikimedia.org/wikipedia/commons/thumb/1/1c/ICloud_logo.svg/2560px-ICloud_logo.svg.png") 
                )
    nodes.append( Node(id="Exist", 
                        label = 'Exist API',
                    size=15,
                    shape="image",
                    image="data:image/png;base64,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") 
                )
    nodes.append( Node(id="Withings", 
                        label = 'Withings API',
                    size=15,
                    shape="image",
                    image="data:image/jpeg;base64,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") 
                )
    nodes.append( Node(id="Watch", 
                        label = 'Apple Watch',
                    size=15,
                    shape="image",
                    image="https://static.nike.com/a/images/f_auto,cs_srgb/w_1536,c_limit/ec8c7fbc-f178-49ea-bd68-a5ddf4218b94/image.jpg") 
                )
    nodes.append( Node(id="Shortcuts", 
                        label = 'iOS Shortcuts',
                    size=15,
                    shape="image",
                    image="data:image/jpeg;base64,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") 
                )
    nodes.append( Node(id="Watch Data", 
                        label = 'Steps, Cals \n& VO2 Max',
                    size=5,
                    shape="dot", color='black') 
                )
    nodes.append( Node(id="Sleep", 
                        label = 'Sleep',
                    size=5,
                    shape="dot", color='black') 
                )
    nodes.append( Node(id="Withings Data", 
                        label = 'Weight & Body Fat',
                    size=5,
                    shape="dot", color='black') 
                )
    nodes.append( Node(id="MyFitnessPal", 
                        label = 'MyFitnessPal',
                    size=15,
                    shape="image", image = "https://upload.wikimedia.org/wikipedia/en/6/63/MyFitnessPal_Logo.png") 
                )
    nodes.append( Node(id="Withings Scale", 
                        label = 'Withings Scale',
                    size=15,
                    shape="image", image = "data:image/jpeg;base64,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") 
                )    
    nodes.append( Node(id="Diet", 
                        label = 'Diet',
                    size=5,
                    shape="dot", color='black') 
                )
    edges.append( Edge(source="Diet", 
                    label="", 
                    target="MyFitnessPal", 
                    ) 
                ) 
    edges.append( Edge(source="Withings Data", 
                    label="", 
                    target="Withings Scale", 
                    ) 
                ) 
    edges.append( Edge(source="Withings Scale", 
                    label="", 
                    target="Withings", 
                    ) 
                ) 
    edges.append( Edge(source="MyFitnessPal", 
                    label="", 
                    target="Shortcuts", 
                    ) 
                ) 
    edges.append( Edge(source="Watch Data", 
                    label="", 
                    target="Watch", 
                    ) 
                ) 
    edges.append( Edge(source="Sleep", 
                    label="", 
                    target="Watch", 
                    ) 
                ) 
    edges.append( Edge(source="Shortcuts", 
                    label="", 
                    target="PyiCloud", 
                    ) 
                ) 
    edges.append( Edge(source="Watch Data", 
                    label="", 
                    target="Watch", 
                    ) 
                ) 
    edges.append( Edge(source="Watch", 
                    label="", 
                    target="Shortcuts", 
                    ) 
                ) 
    edges.append( Edge(source="Watch", 
                    label="", 
                    target="Exist", 
                    ) 
                ) 
    edges.append( Edge(source="Withings", 
                    label="", 
                    target="CSV", 
                    ) 
                ) 
    edges.append( Edge(source="PyiCloud", 
                    label="", 
                    target="CSV", 
                    ) 
                ) 
    edges.append( Edge(source="Exist", 
                    label="", 
                    target="CSV", 
                    ) 
                ) 
    edges.append( Edge(source="Pandas", 
                    label="", 
                    target="Streamlit", 
                    ) 
                ) 
    edges.append( Edge(source="Pandas", 
                    label="", 
                    target="Pyplot", 
                    ) 
                ) 
    edges.append( Edge(source="CSV", 
                    label="", 
                    target="Pandas", 
                    ) 
                ) 

    config = Config(width=700, 
                    height=800, 
                    hierarchical=True
                    ) 
    options = {'autoResize': True,'height': '100%','width': '100%'}

    return_value = agraph(nodes=nodes, edges=edges, config=config)
    return return_value