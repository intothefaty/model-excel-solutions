<template>
  <v-container class="fill-height">
    <v-responsive class="align-centerfill-height mx-auto" max-width="900">
      <v-card title="Yedek Parça Tahmin" flat>
        <template v-slot:text>
          <v-text-field
            v-model="search"
            label="Search"
            prepend-inner-icon="mdi-magnify"
            variant="outlined"
            hide-details
            single-line
          ></v-text-field>
        </template>

        <v-data-table
          :headers="headers"
          :items="spareParts"
          :search="search"
        ></v-data-table>
      </v-card>

      <v-btn
        @click="generate()"
        style="margin-top: 10px"
        rounded="xl"
        size="x-large"
        block
        >Generate</v-btn
      >
    </v-responsive>
  </v-container>
</template>

<script>
import { read, utils } from "xlsx";

export default {
  data() {
    return {
      search: "",
      headers: [
        {
          align: "start",
          key: "Yedek Parça Kodu",
          sortable: false,
          title: "Yedek Parça Kodu",
        },
        { key: "min_error_model", title: "Minimum Error Model" },
        { key: "MAE", title: "MAE" },
      ],
      spareParts: [],
    };
  },
  methods: {
    generate: function () {
      var fileInput = document.createElement("input");
      fileInput.type = "file";
      fileInput.accept = ".xlsx, .xls";

      // Dosya seçildiğinde çalışacak fonksiyon
      fileInput.addEventListener("change", (event) => {
        var file = event.target.files[0];
        var reader = new FileReader();
        reader.onload = (e) => {
          var data = new Uint8Array(e.target.result);
          var workbook = read(data, { type: "array" });
          var sheetName = workbook.SheetNames[0];
          var sheet = workbook.Sheets[sheetName];
          var rows = utils.sheet_to_json(sheet);
          console.log(rows);
          this.spareParts = rows;
        };
        reader.readAsArrayBuffer(file);
      });

      // Dosya seçme penceresini aç
      fileInput.click();
    },
  },
};
</script>
