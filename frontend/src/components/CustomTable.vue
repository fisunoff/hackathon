<template>
  <div class="pa-4">
    <div class="d-flex justify-content-center align-center">
      <span>{{ tableTitle }}</span>
      <v-card-title style="width: 30%">
      <v-text-field
        v-model="search"
        outlined
        dense
        append-icon="mdi-magnify"
        label="Поиск"
        hide-details
      ></v-text-field>
      </v-card-title>
      <template>
        <slot/>
      </template>
      <v-btn v-if="addAction" color="primary" class="ml-auto" @click="addItem">Добавить</v-btn>
    </div>
    <v-data-table
      dense
      :search="search"
      :headers="headers"
      :items="filterItems"
      :footer-props="{
        'items-per-page-options': [10, 25, 50, 100, -1]
      }"
      :items-per-page="50"
      class="elevation-1"
    >
      <template v-slot:item="{ item }">
        <tr>
          <td v-for="(col,index) in headers" :key="index">{{ item[col.value] }}</td>
          <td class="action-cell">
            <v-icon
              v-if="canEdit"
              small
              class="mr-2"
              @click="editItem(item)"
            >
              mdi-pencil
            </v-icon>
            <v-icon
              v-if="canEdit"
              small
              @click="deleteItem(item)"
            >
              mdi-delete
            </v-icon>
          </td>
        </tr>
    </template>
    </v-data-table>
    <custom-modal
        ref="modal"
        :form="useForm"
        :api-path="apiPath"
        :modal-title="modalTitle"
        :value="formValue"
    />
  </div>
</template>

<script>

import CustomModal from "@/components/CustomModal.vue";
import DeleteConfirmation from "@/components/DeleteConfirmation.vue";
import {parse} from "date-fns";

export default {
  name: "CustomTable",
  provide() {
    return {
      $table: this
    }
  },
  components: {CustomModal},
  props: {
    headers: {
      type: Array,
      required: true,
    },
    items: {
      type: Array,
      required: true,
    },
    apiPath: {
      type: String,
      required: true,
    },
    tableTitle: {
      type: String,
      required: false,
    },
    addAction: {
      type: Boolean,
      default: false,
    },
    canEdit: {
      type: Boolean,
      default: false,
    },
    CreateForm: {
      type: Object,
      default: null,
    },
    EditForm: {
      type: Object,
      default: null,
    }
  },
  data() {
    return {
      openModal: false,
      useForm: null,
      modalTitle: null,
      search: '',
      formValue: null,
      DeleteConfirmation: DeleteConfirmation,
      startDate: '1970-01-01',
      endDate: '2077-01-01',
    }
  },
  computed: {
    filterItems() {
      const customFormat = 'yyyy-MM-dd';
      let start = this.startDate
      let end = this.endDate
      if ((start == null && end == null) || start == '' && end == '') {
        start = '1970-01-01'
        end = '2077-01-01'
      }
      console.log(start)
      start = parse(start, customFormat, new Date());
      end = parse(end, customFormat, new Date());
      return this.items.filter(r => parse(r.date_added_new, customFormat, new Date()) >= start &&
            parse(r.date_added_new, customFormat, new Date()) <= end);

    }
  },
  methods: {
    addItem() {
      this.useForm = this.CreateForm
      this.modalTitle = 'Добавить запись'
      this.$refs.modal.dialog = true
    },
    editItem(item) {
      this.useForm = this.EditForm
      this.modalTitle = 'Добавить запись'
      this.formValue = item
      this.$refs.modal.dialog = true
    },
    deleteItem(item) {
      this.useForm = this.DeleteConfirmation
      this.modalTitle = 'Удалить запись'
      this.formValue = item
      this.$refs.modal.dialog = true
    },
  }
}
</script>

<style scoped>
  .action-cell {
    width: 100px;
  }
</style>