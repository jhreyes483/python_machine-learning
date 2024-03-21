$(document).ready(function () {
  $("#btnAll").click(function () {
    $("#all").show("slow");
    $("#filter").hide("slow").removeClass("d-none");
  });

  $("#btnFilter").click(function () {
    $("#filter").show("slow").removeClass("d-none");
    $("#all").hide("slow");
  });

  const getCovid = async () => {
    const response = await axios.get(
      "https://api.covidtracking.com/v1/us/daily.json"
    );
    try {
      if (response.status == 200 && response.data.length > 0) {
        let dateAll = document.getElementById("tbody_all");
        let dateFilter = document.getElementById("tbody_filter");

        if (dateAll) {
          let tableBodyAll = ``;
          response.data.forEach((e) => {
            tableBodyAll += `  <tr>
                                      <td>${e.hospitalized}</td>
                                      <td>${e.positive}</td>
                                      <td>${e.negative}</td>
                                      <td>${e.death}</td>
                                      <td>${e.date}</td>
                                  </tr>
                              `;
          });

          dateAll.innerHTML = tableBodyAll;
        }

        if (dateFilter) {
          let tableBodyFilter = ``;
          let filtered = response.data.filter((e) => e.date > '20210101')
          console.log(filtered)
          filtered.forEach((e) => {

            tableBodyFilter += `  <tr>
                                      <td>${e.date}</td>
                                      <td>${e.death}</td>
                                  </tr>
                              `;
          });

          dateFilter.innerHTML = tableBodyFilter;
        }
      }
    } catch (error) {
      console.log(error);
    }
  };

  getCovid();
});
