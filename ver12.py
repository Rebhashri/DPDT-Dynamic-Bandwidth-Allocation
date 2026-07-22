# ============================================================
# DPDT VERSION 12
# FINAL CONSTRAINT-AWARE DYNAMIC BANDWIDTH ALLOCATION
# ============================================================

TOTAL_BANDWIDTH = 100.0

priority_order = [
    "High",
    "Medium",
    "Low"
]


# ============================================================
# USER DATA FOR EACH TIME INTERVAL
# ============================================================

scenarios = [

    {
        "U1": {"application": "Online Interview", "priority": "High",
               "allocated": 20, "used": 5, "requested": 20},

        "U2": {"application": "Online Class", "priority": "Medium",
               "allocated": 15, "used": 10, "requested": 15},

        "U3": {"application": "YouTube", "priority": "Low",
               "allocated": 30, "used": 30, "requested": 40},

        "U4": {"application": "Gaming", "priority": "Low",
               "allocated": 25, "used": 20, "requested": 35}
    },

    {
        "U1": {"application": "Online Interview", "priority": "High",
               "allocated": 20, "used": 15, "requested": 20},

        "U2": {"application": "Online Class", "priority": "Medium",
               "allocated": 15, "used": 5, "requested": 25},

        "U3": {"application": "YouTube", "priority": "Low",
               "allocated": 30, "used": 25, "requested": 40},

        "U4": {"application": "Gaming", "priority": "Low",
               "allocated": 25, "used": 30, "requested": 35}
    },

    {
        "U1": {"application": "Online Interview", "priority": "High",
               "allocated": 20, "used": 20, "requested": 20},

        "U2": {"application": "Online Class", "priority": "Medium",
               "allocated": 15, "used": 15, "requested": 25},

        "U3": {"application": "YouTube", "priority": "Low",
               "allocated": 30, "used": 20, "requested": 40},

        "U4": {"application": "Gaming", "priority": "Low",
               "allocated": 25, "used": 25, "requested": 35}
    },

    {
        "U1": {"application": "Online Interview", "priority": "High",
               "allocated": 20, "used": 5, "requested": 30},

        "U2": {"application": "Online Class", "priority": "Medium",
               "allocated": 15, "used": 15, "requested": 15},

        "U3": {"application": "YouTube", "priority": "Low",
               "allocated": 30, "used": 30, "requested": 40},

        "U4": {"application": "Gaming", "priority": "Low",
               "allocated": 25, "used": 25, "requested": 35}
    }
]


# ============================================================
# DPDT ALLOCATION FUNCTION
# ============================================================

def dpdt_allocate(users):

    print("Bandwidth Usage Analysis")
    print("------------------------")

    redistribution_pool = 0

    # Calculate unused bandwidth and redistribution pool
    for user_id, user in users.items():

        unused = max(
            user["allocated"] - user["used"],
            0
        )

        additional_demand = max(
            user["requested"] - user["allocated"],
            0
        )

        user["unused"] = unused
        user["additional_demand"] = additional_demand

        redistribution_pool += unused

        print(
            user_id,
            "|",
            user["application"],
            "| Priority:", user["priority"],
            "| Allocated:", round(user["allocated"], 2),
            "Mbps | Used:", user["used"],
            "Mbps | Requested:", user["requested"],
            "Mbps | Unused:", round(unused, 2),
            "Mbps | Additional Demand:",
            round(additional_demand, 2),
            "Mbps"
        )

    print(
        "\nTotal Redistribution Pool:",
        round(redistribution_pool, 2),
        "Mbps"
    )


    # ========================================================
    # DPDT DIAGONAL TRAVERSAL
    # ========================================================

    print("\n========================================")
    print("       DPDT DIAGONAL TRAVERSAL")
    print("========================================")


    available = redistribution_pool


    for priority in priority_order:

        group = []

        for user_id, user in users.items():

            if user["priority"] == priority:
                group.append((user_id, user))


        total_demand = sum(
            user["additional_demand"]
            for user_id, user in group
        )


        print("\nCurrent Node:", priority)
        print(
            "Total Additional Demand:",
            round(total_demand, 2),
            "Mbps"
        )

        print(
            "Available Bandwidth:",
            round(available, 2),
            "Mbps"
        )


        # ----------------------------------------------------
        # CASE 1: NO ADDITIONAL DEMAND
        # ----------------------------------------------------

        if total_demand == 0:

            print(
                "Decision: No additional demand."
            )

            print(
                "Diagonal transition → Next priority."
            )

            continue


        # ----------------------------------------------------
        # CASE 2: ENOUGH BANDWIDTH
        # ----------------------------------------------------

        if available >= total_demand:

            print(
                "Decision: Full demand can be satisfied."
            )

            for user_id, user in group:

                allocation = user["additional_demand"]

                user["allocated"] += allocation

                available -= allocation

                print(
                    user_id,
                    "received",
                    round(allocation, 2),
                    "Mbps"
                )


        # ----------------------------------------------------
        # CASE 3: INSUFFICIENT BANDWIDTH
        # ----------------------------------------------------

        else:

            print(
                "Decision: Insufficient bandwidth."
            )

            print(
                "Applying demand proportional sharing."
            )


            if total_demand > 0:

                for user_id, user in group:

                    share = (
                        user["additional_demand"]
                        /
                        total_demand
                    ) * available

                    allocation = min(
                        share,
                        user["additional_demand"]
                    )

                    user["allocated"] += allocation

                    print(
                        user_id,
                        "received",
                        round(allocation, 2),
                        "Mbps"
                    )


            available = 0

            print(
                "Redistribution pool exhausted."
            )

            break


    # ========================================================
    # FINAL CAPACITY VALIDATION
    # ========================================================

    total_allocated = sum(
        user["allocated"]
        for user in users.values()
    )


    # Small floating-point correction
    if abs(total_allocated - TOTAL_BANDWIDTH) < 0.000001:

        total_allocated = TOTAL_BANDWIDTH


    # Safety check
    if total_allocated > TOTAL_BANDWIDTH:

        excess = (
            total_allocated
            - TOTAL_BANDWIDTH
        )

        print(
            "\nWARNING: Allocation exceeded network capacity."
        )

        print(
            "Applying final capacity correction."
        )


        # Reduce allocation starting from
        # lowest priority users
        for priority in reversed(priority_order):

            for user_id, user in users.items():

                if excess <= 0:
                    break

                if user["priority"] == priority:

                    reducible = max(
                        user["allocated"]
                        - user["used"],
                        0
                    )

                    reduction = min(
                        reducible,
                        excess
                    )

                    user["allocated"] -= reduction

                    excess -= reduction

            if excess <= 0:
                break


        total_allocated = sum(
            user["allocated"]
            for user in users.values()
        )


    remaining_bandwidth = max(
        TOTAL_BANDWIDTH
        - total_allocated,
        0
    )


    # ========================================================
    # FINAL OUTPUT
    # ========================================================

    print("\n========================================")
    print("       FINAL DPDT ALLOCATION")
    print("========================================")


    for user_id, user in users.items():

        print(
            user_id,
            "|",
            user["application"],
            "| Priority:", user["priority"],
            "| Final Allocation:",
            round(user["allocated"], 2),
            "Mbps"
        )


    print(
        "\nTotal Allocated Bandwidth:",
        round(total_allocated, 2),
        "Mbps"
    )


    print(
        "Remaining Network Bandwidth:",
        round(remaining_bandwidth, 2),
        "Mbps"
    )


    # Capacity validation
    if total_allocated <= TOTAL_BANDWIDTH:

        print(
            "Capacity Check: PASSED"
        )

    else:

        print(
            "Capacity Check: FAILED"
        )


# ============================================================
# MAIN SIMULATION
# ============================================================

print("========================================")
print("       DPDT VERSION 12")
print(" FINAL CONSTRAINT-AWARE ALLOCATION")
print("========================================")


for interval, scenario in enumerate(
    scenarios,
    start=1
):

    print(
        "\n\n============================================================"
    )

    print(
        "TIME INTERVAL",
        interval
    )

    print(
        "============================================================"
    )


    dpdt_allocate(scenario)


    print(
        "\nNote: Each time interval represents a new network demand state."
    )


print(
    "\n\n========================================"
)

print(
    "       DPDT SIMULATION COMPLETED"
)

print(
    "========================================"
)