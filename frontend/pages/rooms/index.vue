<template>
  <div>
    <v-row class="mt-12 mainRow d-flex justify-center">
      <v-col md="8" sm="7" class>
        <v-card max-width="1400" height="100" class="pa-2 filterCard"> </v-card>
      </v-col>

      <v-col md="8" sm="7">
        <v-card max-width="1400" height="500" class="pa-2 itemCard">
          <rooms-list-item
            v-for="room in rooms"
            :key="room.id"
            :id="room.id"
            :number="(num += 1)"
            :title="room.title"
            :image="room.image"
            :lastUpdated="room.lastUpdated"
            :updatedBy="room.updatedBy"
          >
          </rooms-list-item>
        </v-card>
        <v-pagination
          id="pagination"
          class="mt-8"
          color="primary"
        ></v-pagination>
      </v-col>

      <v-container class="justify-center d-flex">
        <v-dialog v-model="roomDialog" max-width="600px">
          <template v-slot:activator="{ on, attrs }">
            <v-btn v-bind="attrs" v-on="on" color="primary">Create Room</v-btn>
          </template>
          <create-room-dialog></create-room-dialog>
        </v-dialog>
      </v-container>
    </v-row>
  </div>
</template>

<script>
import RoomsListItem from '~/components/RoomsListItem.vue';
import CreateRoomDialog from '~/components/dialogs/CreateRoomDialog.vue';

export default {
  components: { RoomsListItem, CreateRoomDialog },
  data() {
    return {
      roomDialog: false,
      num: 0,
      rooms: [],
    };
  },
  created() {
    this.rooms = this.$store.getters['rooms/getRooms'];
  },
};
</script>

<style scoped>
li {
  list-style-type: none;
}
/* #pagination {
    position: absolute;
    bottom: 0;
    left: 0;
    right: 0;
    margin-bottom: 1.5rem;
  } */

/* a {
    text-decoration: none;
    color: #006400;
  } */

/* Smartphones */
/* @media (max-width: 767px) {
    .itemCard {
      height: 1300px !important;
    }
    .mainRow {
      margin-top: 0px !important;
    }
  }
   */
/* Tablets */
/* @media (min-width: 768px) and (max-width: 991px) {
    .mainRow {
      justify-content: center;
    }
  }
  
  /* Desktop */
/* @media (min-width: 992px) {
    .filterCard {
      margin-left: 25px;
    }
  } */
</style>
