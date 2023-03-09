from streamlit_agraph import agraph, Node, Edge, Config    
        
def health_visual():

    nodes = []
    edges = []
    nodes.append( Node(id="Pandas", 
                    label="Pandas", 
                    size=15, font={'color':'white'},
                    shape="image",
                    image="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQVjjK7uT1yLWjWfIZ7dW5Bvmvs-e5DsZZPwix4SrA&s") 
                ) # includes **kwargs
    nodes.append( Node(id="Streamlit", 
                        label = 'Streamlit',
                    size=15,font={'color':'white'},
                    shape="image",
                    image="https://streamlit.io/images/brand/streamlit-mark-color.svg", ) 
                )
    nodes.append( Node(id="Pyplot", 
                        label = 'Pyplot',
                    size=15,font={'color':'white'},
                    shape="image",
                    image="https://cdn.theorg.com/39deb29f-6dae-4ac1-940c-39515deac1e5_medium.jpg" ) 
                )     
    nodes.append( Node(id="Python", 
                        label = 'Python',
                    size=15,font={'color':'white'},
                    shape="image",
                    image="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/1869px-Python-logo-notext.svg.png" ) 
                )     
    nodes.append( Node(id="CSV", 
                        label = 'CSV',
                    size=15,font={'color':'white'},
                    shape="image",
                    image="https://cdn-icons-png.flaticon.com/512/6133/6133884.png") 
                )
    nodes.append( Node(id="PyiCloud", 
                        label = 'PyiCloud API',
                    size=15,font={'color':'white'},
                    shape="image",
                    image="https://upload.wikimedia.org/wikipedia/commons/thumb/1/1c/ICloud_logo.svg/2560px-ICloud_logo.svg.png") 
                )
    nodes.append( Node(id="Exist", 
                        label = 'Exist API',
                    size=15,font={'color':'white'},
                    shape="image",
                    image="data:image/png;base64,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") 
                )
    nodes.append( Node(id="Withings", 
                        label = 'Withings API',
                    size=15,font={'color':'white'},
                    shape="image",
                    image="data:image/jpeg;base64,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") 
                )
    nodes.append( Node(id="Watch", 
                        label = 'Apple Watch',
                    size=15,font={'color':'white'},
                    shape="image",
                    image="https://static.nike.com/a/images/f_auto,cs_srgb/w_1536,c_limit/ec8c7fbc-f178-49ea-bd68-a5ddf4218b94/image.jpg") 
                )
    nodes.append( Node(id="Shortcuts", 
                        label = 'iOS Shortcuts',
                    size=15,
                    shape="image",font={'color':'white'},
                    image="data:image/jpeg;base64,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") 
                )
    nodes.append( Node(id="Watch Data", 
                        label = 'Steps, Cals, \n Sleep & VO2 Max',
                    size=5,font={'color':'white'},
                    shape="dot", color='white') 
                )
    nodes.append( Node(id="Withings Data", 
                        label = 'Weight & Body Fat',
                    size=5,font={'color':'white'},
                    shape="dot", color='white') 
                )
    nodes.append( Node(id="MyFitnessPal", 
                        label = 'MyFitnessPal',
                    size=15,font={'color':'white'},
                    shape="image", image = "https://upload.wikimedia.org/wikipedia/en/6/63/MyFitnessPal_Logo.png") 
                )
    nodes.append( Node(id="Withings Scale", 
                        label = 'Withings Scale',
                    size=15,font={'color':'white'},
                    shape="image", image = "data:image/jpeg;base64,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") 
                )    
    nodes.append( Node(id="Diet", 
                        label = 'Diet',font={'color':'white'},
                    size=5,
                    shape="dot", color='white') 
                )      
    edges.append( Edge(source="Python", 
                    label="", 
                    target="CSV", 
                    color='white') 
                ) 
    edges.append( Edge(source="Diet", 
                    label="", 
                    target="MyFitnessPal", 
                    color='white') 
                ) 
    edges.append( Edge(source="Withings Data", 
                    label="", 
                    target="Withings Scale", color='white'
                    ) 
                ) 
    edges.append( Edge(source="Withings Scale", 
                    label="", 
                    target="Withings", color='white'
                    ) 
                ) 
    edges.append( Edge(source="MyFitnessPal", 
                    label="", 
                    target="Shortcuts", color='white'
                    ) 
                ) 
    edges.append( Edge(source="Watch Data", 
                    label="", 
                    target="Watch", 
                    color='white' 
                    ) 
                ) 
    edges.append( Edge(source="Shortcuts", 
                    label="", 
                    target="PyiCloud", color='white'
                    ) 
                ) 
    edges.append( Edge(source="Watch Data", 
                    label="", 
                    target="Watch", color='white'
                    ) 
                ) 
    edges.append( Edge(source="Watch", 
                    label="", 
                    target="Shortcuts", color='white'
                    ) 
                ) 
    edges.append( Edge(source="Watch", 
                    label="", 
                    target="Exist", color='white'
                    ) 
                ) 
    edges.append( Edge(source="Withings", 
                    label="", 
                    target="Python", color='white'
                    ) 
                ) 
    edges.append( Edge(source="PyiCloud", 
                    label="", 
                    target="Python", color='white'
                    ) 
                ) 
    edges.append( Edge(source="Exist", 
                    label="",  
                    target="Python", color='white'
                    ) 
                ) 
    edges.append( Edge(source="Pandas", 
                    label="", 
                    target="Streamlit", color='white'
                    ) 
                ) 
    edges.append( Edge(source="Pandas", 
                    label="", 
                    target="Pyplot", color='white'
                    ) 
                ) 
    edges.append( Edge(source="CSV", 
                    label="", 
                    target="Pandas", color='white'
                    ))
 
    config = Config( width=700, 
                    height=800, 
                    hierarchical=True,  
                    )

    return_value = agraph(nodes=nodes, edges=edges, config=config)
    
    return return_value

def productivity_visual():
    nodes = []
    edges = []
    nodes.append( Node(id="Tracking", 
                    label="TrackingTime API", 
                    size=10, font={'color':'white'},
                    shape="image",
                    image="https://trackingtime.co/wp-content/uploads/2022/09/TrackingTime-logo-complete.png") 
                )
    nodes.append( Node(id="Waka", 
                label="WakaTime API", 
                size=15, font={'color':'white'},
                shape="image",
                image="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQra-BSlYIkhhuSxGEZ6rYVqoJojLDL-3wuXPEtul4U5lnHooSGaR4JtcNEk_57eIuj5jI&usqp=CAU") 
            )
    nodes.append( Node(id="Exist", 
                label="Exist API", 
                size=15, font={'color':'white'},
                shape="image",
                image="data:image/png;base64,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") 
            )
    nodes.append( Node(id="Pandas", 
                    label="Pandas", 
                    size=15, font={'color':'white'},
                    shape="image",
                    image="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQVjjK7uT1yLWjWfIZ7dW5Bvmvs-e5DsZZPwix4SrA&s") 
                ) # includes **kwargs
    nodes.append( Node(id="Streamlit", 
                        label = 'Streamlit',
                    size=15,font={'color':'white'},
                    shape="image",
                    image="https://streamlit.io/images/brand/streamlit-mark-color.svg", ) 
                )
    nodes.append( Node(id="Pyplot", 
                        label = 'Pyplot',
                    size=15,font={'color':'white'},
                    shape="image",
                    image="https://cdn.theorg.com/39deb29f-6dae-4ac1-940c-39515deac1e5_medium.jpg" ) 
                )     
    nodes.append( Node(id="Python", 
                        label = 'Python',
                    size=15,font={'color':'white'},
                    shape="image",
                    image="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/1869px-Python-logo-notext.svg.png" ) 
                )     
    nodes.append( Node(id="CSV", 
                        label = 'CSV',
                    size=15,font={'color':'white'},
                    shape="image",
                    image="https://cdn-icons-png.flaticon.com/512/6133/6133884.png") 
                )
    nodes.append( Node(id="Hrs", 
                        label = 'Reading & \n Work Hours',font={'color':'white'},
                    size=5,
                    shape="dot", color='white') 
                )
    nodes.append( Node(id="Coding Hrs", 
                        label = 'Coding Hours',font={'color':'white'},
                    size=5,
                    shape="dot", color='white') 
                )
    nodes.append( Node(id="Git", 
                        label = 'GitHub Commits',font={'color':'white'},
                    size=5,
                    shape="dot", color='white') 
                )
    edges.append( Edge(source="Exist", 
                    label="",  
                    target="Python", color='white'
                    ) 
                ) 
    edges.append( Edge(source="Pandas", 
                    label="", 
                    target="Streamlit", color='white'
                    ) 
                ) 
    edges.append( Edge(source="Pandas", 
                    label="", 
                    target="Pyplot", color='white'
                    ) 
                ) 
    edges.append( Edge(source="CSV", 
                    label="", 
                    target="Pandas", color='white'
                    ))
    edges.append( Edge(source="Python", 
                    label="", 
                    target="CSV", 
                    color='white') )
    edges.append( Edge(source="Waka", 
                    label="",  
                    target="Python", color='white'
                    ) 
                )             
    edges.append( Edge(source="Tracking", 
                    label="",  
                    target="Python", color='white'
                    ) 
                )     
    edges.append( Edge(source="Hrs", 
                    label="",  
                    target="Tracking", color='white'
                    ) 
                ) 
    edges.append( Edge(source="Coding Hrs", 
                    label="",  
                    target="Waka", color='white'
                    ) 
                ) 
    edges.append( Edge(source="Git", 
                    label="",  
                    target="Exist", color='white'
                    ) 
                )     
    config = Config( width=700, 
                    height=800, 
                    hierarchical=True,  
                    )

    return_value = agraph(nodes=nodes, edges=edges, config=config)
    
    return return_value

def personal_visual():
    nodes = []
    edges = []
    nodes.append( Node(id="Pandas", 
                        label="Pandas", 
                        size=15, font={'color':'white'},
                        shape="image",
                        image="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQVjjK7uT1yLWjWfIZ7dW5Bvmvs-e5DsZZPwix4SrA&s") 
                    ) # includes **kwargs
    nodes.append( Node(id="Streamlit", 
                        label = 'Streamlit',
                    size=15,font={'color':'white'},
                    shape="image",
                    image="https://streamlit.io/images/brand/streamlit-mark-color.svg", ) 
                )
    nodes.append( Node(id="Pyplot", 
                        label = 'Pyplot',
                    size=15,font={'color':'white'},
                    shape="image",
                    image="https://cdn.theorg.com/39deb29f-6dae-4ac1-940c-39515deac1e5_medium.jpg" ) 
                )     
    nodes.append( Node(id="Python", 
                        label = 'Python',
                    size=15,font={'color':'white'},
                    shape="image",
                    image="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/1869px-Python-logo-notext.svg.png" ) 
                )     
    nodes.append( Node(id="CSV", 
                        label = 'CSV',
                    size=15,font={'color':'white'},
                    shape="image",
                    image="https://cdn-icons-png.flaticon.com/512/6133/6133884.png") 
                )
    nodes.append( Node(id="Exist", 
                label="Exist API", 
                size=15, font={'color':'white'},
                shape="image",
                image="data:image/png;base64,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") 
            )
    nodes.append( Node(id="Airtable", 
                label="Airtable API", 
                size=15, font={'color':'white'},
                shape="image",
                image="https://www.airtable.com/images/newsroom/newsroom_image-1_1x.png") 
            )
    nodes.append( Node(id="Spotify", 
                label="Spotify API", 
                size=25, font={'color':'white'},
                shape="image",
                image="data:image/png;base64,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") 
            )
    nodes.append( Node(id="Todoist", 
                label="ToDoist API", 
                size=13, font={'color':'white'},
                shape="image",
                image="https://upload.wikimedia.org/wikipedia/commons/6/6d/Todoist_logo.png") 
            )
    nodes.append( Node(id="Mood", 
                        label = 'Mood Data',font={'color':'white'},
                    size=5,
                    shape="dot", color='white') 
                )      
    nodes.append( Node(id="Books", 
                        label = 'Reading & Book Data',font={'color':'white'},
                    size=5,
                    shape="dot", color='white') 
                )      
    nodes.append( Node(id="Music", 
                        label = 'Listening Data',font={'color':'white'},
                    size=5,
                    shape="dot", color='white') 
                )      
    nodes.append( Node(id="Todos", 
                        label = "ToDo's Completed",font={'color':'white'},
                    size=5,
                    shape="dot", color='white') 
                )      
    edges.append( Edge(source="Exist", 
                    label="",  
                    target="Python", color='white'
                    ) 
                ) 
    edges.append( Edge(source="Pandas", 
                    label="", 
                    target="Streamlit", color='white'
                    ) 
                ) 
    edges.append( Edge(source="Pandas", 
                    label="", 
                    target="Pyplot", color='white'
                    ) 
                ) 
    edges.append( Edge(source="CSV", 
                    label="", 
                    target="Pandas", color='white'
                    ))
    edges.append( Edge(source="Python", 
                    label="", 
                    target="CSV", 
                    color='white') )
    edges.append( Edge(source="Airtable", 
                    label="", 
                    target='Streamlit', 
                    color='white') )
    edges.append( Edge(source="Spotify", 
                    label="", 
                    target="Streamlit", 
                    color='white') )
    edges.append( Edge(source="Todoist", 
                    label="", 
                    target="Python", 
                    color='white') )
    edges.append( Edge(source="Mood", 
                    label="", 
                    target="Exist", 
                    color='white') )
    edges.append( Edge(source="Books", 
                    label="", 
                    target="Airtable", 
                    color='white') )
    edges.append( Edge(source="Music", 
                    label="", 
                    target="Spotify", 
                    color='white') )
    edges.append( Edge(source="Todos", 
                    label="", 
                    target="Todoist", 
                    color='white') )
    config = Config( width=700, 
                    height=800, 
                    hierarchical=True,  
                    )

    return_value = agraph(nodes=nodes, edges=edges, config=config)
    
    return return_value

def welcome_visual():
    nodes = []
    edges = []
    nodes.append( Node(id="Python", 
                    label = 'Python',
                size=15,font={'color':'white'},
                shape="image",
                image="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/1869px-Python-logo-notext.svg.png" ) 
            )     
    nodes.append( Node(id="Streamlit", 
                        label = 'Streamlit',
                    size=15,font={'color':'white'},
                    shape="image",
                    image="https://streamlit.io/images/brand/streamlit-mark-color.svg", ) 
                )
    nodes.append( Node(id="Spotify", 
                label="Spotify API", 
                size=25, font={'color':'white'},
                shape="image",
                image="data:image/png;base64,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") 
            )
    nodes.append( Node(id="Todoist", 
                label="ToDoist API", 
                size=13, font={'color':'white'},
                shape="image",
                image="https://upload.wikimedia.org/wikipedia/commons/6/6d/Todoist_logo.png") 
            )
    nodes.append( Node(id="Sports", 
                label="Football API", 
                size=15, font={'color':'white'},
                shape="image",
                image="https://api-sports.io/assets/img/home1/hero-banner.png") 
            )
    nodes.append( Node(id="TFL", 
                label="TFL API", 
                size=15, font={'color':'white'},
                shape="image",
                image="https://camo.githubusercontent.com/2fbe9828475e6b419546ec47be120a0e6e8dfc6e3d8d3c433463817a57c0e977/68747470733a2f2f626c6f672e74666c2e676f762e756b2f77702d636f6e74656e742f75706c6f6164732f323031382f30352f63726f707065642d6c6f676f5f726f756e64656c2d322e706e67") 
            )
    nodes.append( Node(id="Weather API", 
                label="Weather API", 
                size=15, font={'color':'white'},
                shape="image",
                image="data:image/png;base64,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") 
            )
    nodes.append( Node(id="Music", 
                        label = 'Listening Data',font={'color':'white'},
                    size=5,
                    shape="dot", color='white') 
                )      
    nodes.append( Node(id="United", 
                        label = 'Next ManU Game',font={'color':'white'},
                    size=5,
                    shape="dot", color='white') 
                )      
    nodes.append( Node(id="Weather", 
                        label = 'Current Weather',font={'color':'white'},
                    size=5,
                    shape="dot", color='white') 
                )      
    nodes.append( Node(id="Todos", 
                        label = 'Todos Task List',font={'color':'white'},
                    size=5,
                    shape="dot", color='white') 
                )      
    nodes.append( Node(id="Tube", 
                        label = 'Tube Status',font={'color':'white'},
                    size=5,
                    shape="dot", color='white') 
                )      
    edges.append( Edge(source="Todos", 
                    label="", 
                    target="Todoist", 
                    color='white') )
    edges.append( Edge(source="Weather", 
                    label="", 
                    target="Weather API", 
                    color='white') )
    edges.append( Edge(source="Music", 
                    label="", 
                    target="Spotify", 
                    color='white') )
    edges.append( Edge(source="Python", 
                    label="", 
                    target="Streamlit", 
                    color='white') )
    edges.append( Edge(source="Tube", 
                    label="", 
                    target="TFL", 
                    color='white') )
    edges.append( Edge(source="Python", 
                    label="", 
                    target="Streamlit", 
                    color='white') )
    edges.append( Edge(source="Sports", 
                    label="", 
                    target="Python", 
                    color='white') )
    edges.append( Edge(source="United", 
                    label="", 
                    target="Sports", 
                    color='white') )
    edges.append( Edge(source="Weather API", 
                    label="", 
                    target="Python", 
                    color='white') )
    edges.append( Edge(source="Spotify", 
                    label="", 
                    target="Python", 
                    color='white') )
    edges.append( Edge(source="Todoist", 
                    label="", 
                    target="Python", 
                    color='white') )
    edges.append( Edge(source="TFL", 
                    label="", 
                    target="Python", 
                    color='white') )
    config = Config( width=700, 
                    height=800, 
                    hierarchical=True,  
                    )

    return_value = agraph(nodes=nodes, edges=edges, config=config)
    
    return return_value

                                        