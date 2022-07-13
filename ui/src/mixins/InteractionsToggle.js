import { EventBus } from "@/EventBus";

export const InteractionsToggle = {
  created() {
    const me = this;
    EventBus.$on("on-interaction-activated", (activatedInteraction) => {
      if (activatedInteraction !== me.interactionType) {
        if (me.stop) {
          me.stop();
        }
      }
    });
  },
};
