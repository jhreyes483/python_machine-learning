<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8" />
  <meta http-equiv="X-UA-Compatible" content="IE=edge" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Document</title>
  <?php include_once('./dependency.php') ?>
</head>

<body class="p-0 m-0">
  <div class="row p-5 m-0">
    <div class="col">
      <div class="card shadow">
        <div class="card-header">
          <h3 class="font-weight-bold">API COVID 19 (patrón)</h3>
        </div>
        <div class="card-body">
          <div class="row-reverse">
            <div class="col my-3">
              <div class="row">
                <div class="col-auto">
                  <button class="btn btn-primary" id="btnAll">Estadistica</button>
                </div>
                <div class="col-auto">
                  <button class="btn btn-primary" id="btnFilter">Filtro por año</button>
                </div>
              </div>
            </div>
            <div class="col">
              <table class="table" id="all">
                <thead>
                  <tr>
                    <th scope="col">Hospitalizados</th>
                    <th scope="col">Positivos</th>
                    <th scope="col">Negativos</th>
                    <th scope="col">Muertos</th>
                    <th scope="col">Fecha de registro</th>
                  </tr>
                </thead>
                <tbody id="tbody_all"></tbody>
              </table>
              <table class="table d-none" id="filter">
                <thead>
                  <tr>
                    <th scope="col">Fecha de registro</th>
                    <th scope="col">Numero de fallecidos</th>
                  </tr>
                </thead>
                <tbody id="tbody_filter"></tbody>
              </table>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</body>

</html>