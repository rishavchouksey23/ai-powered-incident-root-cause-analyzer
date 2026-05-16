
package com.incident.controller;

import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/incident")
public class IncidentController {

    @PostMapping("/analyze")
    public String analyze(@RequestBody String payload) {
        return "Incident received for analysis";
    }
}
