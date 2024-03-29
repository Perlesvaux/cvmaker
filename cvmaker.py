#!/usr/bin/env python3

body = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <!-- Bootstrap 5.3.2 -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-C6RzsynM9kWDrMNeT87bh95OGNyZPhcTNXj1NW7RuBCsyN/o0jlpcV8Qyq46cDfL" crossorigin="anonymous"></script>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.1/font/bootstrap-icons.css" integrity="sha384-4LISF5TTJX/fLmGSxO53rV4miRxdg84mZsxmO8Rx5jGtp/LbrixFETvWa5a6sESd" crossorigin="anonymous">


    <style>
    {pagebreak}

    {style}

    </style>

    <title>cvmaker</title>
</head>
<body>


<div class="card border-light mb-3">
  <!-- <div class="card-header text-dark text-center">Name Goes Here</div> -->
      <div class="card-header text-dark text-center h1"><i class="bi bi-person-fill"></i> <span class="px-2">{name}</span></div>

  <div class="card-body">
    <ul class="list-group mb-3">
      <li class="list-group-item list-group-item-info d-flex">
                <i class="bi bi-geo-alt-fill"></i> <span class="px-2">{residence}</span>
      </li>
      <li class="list-group-item list-group-item-info d-flex">
                <i class="bi bi-telephone-fill"></i> <span class="px-2">{phone}</span>
      </li>
      <li class="list-group-item list-group-item-info d-flex">
                <i class="bi bi-envelope-fill"></i> <span class="px-2">{email}</span>
      </li>
    </ul>   
   <div class="row">
            <div class="col-6">
    <a href="{github}" class="btn btn-dark btn-lg p-2  col-12 "><i class="bi bi-github h1"></i></a> 
  </div>

            <div class="col-6">
    <a href="{linkedin}" class="btn btn-info btn-lg p-2  col-12"><i class="bi bi-linkedin h1"></i></a> 
  </div>
  </div>

  </div>
</div>


<div class="card border-light mb-3">
    <div class="card-header text-center h2 text-dark">Skills</div>
     <div class="card-body">
    <ul class="list-group">
      {skills}
    </ul>   
      </div>
</div>


<div class="card border-light mb-3">
    <div class="card-header text-center h2 text-dark">Profile</div>
     <div class="card-body">
        <div class="alert alert-dismissible alert-info">
            {profile}
        </div>
      </div>
</div>

<div class="break"></div>

<div class="card border-light mb-3">
    <div class="card-header text-center h2 text-dark">Licenses & certifications</div>
     <div class="card-body">
        <div class="container d-flex flex-wrap">
          {certifications}
          
        </div>
      </div>
</div>

<div class="break"></div>


<div class="card border-light mb-3">
    <div class="card-header text-center h2 text-dark">Experience</div>
     <div class="card-body">

    <ul class="list-group">
      {experience}
          </ul>

      </div>
</div>





</body>
</html>

"""

import json

import argparse


def main():
    parser = argparse.ArgumentParser(description='Turn a JSON file into a cv! (1) Pipe the output to an HTML file. (2) Open it and do CTRL+P to generate a PDF out of it! ')

    # Positional argument for the file name
    parser.add_argument('json', help='Name of the file')

    # Optional argument to specify image size
    parser.add_argument('-i', '--image-size', type=int, help='Image size', choices=[0,1,2])

    # Optional argument to specify flavor
    parser.add_argument('-f','--flavor', help='Flavor of the script', choices=[
"zephyr","yeti","vapor","united","superhero","spacelab","solar","slate","sketchy","simplex","sandstone","quartz","pulse",
"morph","minty","materia","lux","lumen","litera","journal","flatly","darkly","cyborg","cerulean","cosmo"])

    args = parser.parse_args()

    sizes = ['33', '50', '100']

    img_size = sizes[args.image_size] if args.image_size else '33'

    flavor = f'./styles/{args.flavor}.css' if args.flavor else './styles/spacelab.css'

    with open(args.json, 'r') as file, open(flavor) as css:
        cv = json.load(file)
        style = css.read()
        result = body.format(
            style=style,    
            pagebreak="@media print {.break {page-break-after: always;}}",
            name=cv["name"],
            residence=cv["residence"],
            phone=cv["phone"],
            email=cv["email"],
            github=cv["github"],
            linkedin=cv["linkedin"],
            profile=cv["profile"],
            skills = " ".join ([f"<li class='list-group-item list-group-item-success d-flex'>{skill}</li>" for skill in cv["skills"]]),
            certifications = " ".join([f"<div style='height:{img_size}%;width:{img_size}%;'><a href='{cert['link']}'><img style='height:100%;width:100%; class='border border-dark' src='{cert['file']}'></a></div>" for cert in cv["certifications"]]),
            experience = " ".join([f"<li class='list-group-item list-group-item-primary d-flex'><div class='container'><div class='row'><div class='col-4'><strong> {exp['when']} </strong></div><div class='col-4'><strong>{exp['where']}</strong></div><div class='col-4'><i><strong>{exp['what']}</strong></i></div></div><div>{exp[ 'description' ]}</div></div></li>" for exp in cv['experience']])

            )
        print(result)



if __name__ == "__main__":
    main()

#TODO add 'break' within style 
# Profile MUST BE 59 words or less
