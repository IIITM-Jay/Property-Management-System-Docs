Flow Sequence - Login/ Register
======================


.. graphviz::
   :align: center

   digraph {
      a->b
      b->d [label="Yes", labelfontcolor=green]
      b->c [label="No", labelfontcolor=red]
      d->c 
      c->e
      e->f [label="Yes"]
      e->g [label="No"]
      g->c
      a [shap=ellipse, peripheries=2,color= lightseagreen, label="Property Management System", style=filled, fontcolor=white];
      b [shape=diamond, label="New User" color="lightgray", style=filled]
      c [shape=box, label="Login",peripheries=2, height=0.25, width=1.5, color=springgreen,style=filled, fontcolor=black ]
      d [shape=box, label="Register", height=0.25, width=2, color=orangered,style=filled, fontcolor=white ]
      e [shape=diamond, label="Authorised", color=indigo, fontcolor=white, style=filled]
      f [shape=box, label="Grant Access", peripheries=2,color=lawngreen, fontcolor=white, style=filled, fontcolor=black ]
      g [shape=box, label="Check Your Credentials", width=2, color=  lightcyan, style=filled ,fontcolor=black ]


      
   }
