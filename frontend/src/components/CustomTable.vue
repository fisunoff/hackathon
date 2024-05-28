<template>
  <div>
    <span>Заголовок</span>
    <v-btn color="primary" @click="addItem">Добавить</v-btn>
    <v-data-table dense
      :headers="headers"
      :items="items"
      class="elevation-1"
    >
      <template v-slot:item="{ item }">
        <tr>
          <td v-for="(col,index) in headers" :key="index">{{ item[col.value] }}</td>
          <td>
            <v-icon
              small
              class="mr-2"
              @click="editItem(item)"
            >
              mdi-pencil
            </v-icon>
          </td>
          <td>
            <v-icon
              small
              @click="deleteItem(item)"
            >
              mdi-delete
            </v-icon>
          </td>
        </tr>
    </template>
    </v-data-table>
    <custom-modal ref="modal"/>
  </div>
</template>

<script>

import CustomModal from "@/components/CustomModal.vue";

export default {
  name: "CustomTable",
  components: {CustomModal},
  props: {
    headers: {
      type: Array,
      required: true,
    },
    items: {
      type: Array,
      required: true,
    }
  },
  data() {
    return {
      openModal: false,
    }
  },
  mounted() {
    console.log(this.items)
  },
  methods: {
    addItem() {
      this.$refs.modal.dialog = true
      // this.$ajax.post(`test_case/api/`, {...this.item})
      //     .then(() => {
      //       console.log(111)
      //     })
    },
    editItem(item) {
      console.log('Editing:', item);
    },
    deleteItem(item) {
      console.log('Deleting:', item);
    },
    }
}
</script>

<style scoped>

</style>