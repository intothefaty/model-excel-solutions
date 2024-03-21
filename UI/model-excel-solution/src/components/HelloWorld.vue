<template>
  <v-container class="fill-height">
    <v-responsive class="align-centerfill-height mx-auto" max-width="1500">
      <v-card title="Yedek Parça Tahmin" flat>
        <template v-slot:text>
          <v-text-field v-model="search" label="Search" prepend-inner-icon="mdi-magnify" variant="outlined" hide-details
            single-line></v-text-field>
        </template>

        <v-data-table :headers="headers" :items="spareParts" :search="search"></v-data-table>
      </v-card>

      <v-btn @click="generate()" style="margin-top: 10px" rounded="xl" size="x-large" block>Generate</v-btn>
    </v-responsive>
  </v-container>
</template>

<script>
import { read, utils } from "xlsx";
import axios from 'axios';

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
        { key: "MAE", title: "MAE" }
      ],
      spareParts: [],
      rows: NaN,
      head: NaN
    };
  },
  methods: {
    generate: async function () {
      var fileInput = document.createElement("input");
      fileInput.type = "file";
      fileInput.accept = ".xlsx, .xls";

      // Dosya seçildiğinde çalışacak fonksiyon
      fileInput.addEventListener("change", async (event) => {
        var file = event.target.files[0];
        var reader = new FileReader();
        reader.onload = async (e) => {
          var data = new Uint8Array(e.target.result);
          var workbook = read(data, { type: "array" });
          var sheetName = workbook.SheetNames[0];
          var sheet = workbook.Sheets[sheetName];
          var rows = utils.sheet_to_json(sheet);
          console.log(rows)
          var response = NaN;
          try {
            response = await axios.post('http://localhost:8000/veri_al/', {
              data: rows
            });
            console.log(response.data);
          } catch (error) {
            console.error('Hata:', error);
          }

          rows = response.data;
          var head = Object.keys(rows[0]);

          for (let i = 3; i < head.length; i++) {
            try {
              this.headers.push({
                key: head[i],
                title: head[i],
              });
            } catch (error) { }
          }
          this.spareParts = rows
        };
        reader.readAsArrayBuffer(file);
      });

      // Dosya seçme penceresini aç
      fileInput.click();
    },

  },
};
</script>
