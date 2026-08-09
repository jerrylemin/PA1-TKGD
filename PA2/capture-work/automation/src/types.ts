export type CaptureAction =
  | {
      type: "wait";
      milliseconds: number;
    }
  | {
      type: "clickRole";
      role: "button" | "link" | "tab" | "menuitem";
      name: string;
      exact?: boolean;
    }
  | {
      type: "clickText";
      text: string;
      exact?: boolean;
    }
  | {
      type: "clickLocator";
      selector: string;
    }
  | {
      type: "hover";
      selector: string;
    }
  | {
      type: "press";
      key: string;
    }
  | {
      type: "fill";
      selector: string;
      value: string;
    }
  | {
      type: "selectOption";
      selector: string;
      value: string;
    }
  | {
      type: "waitForText";
      text: string;
    }
  | {
      type: "waitForUrl";
      urlPattern: string;
    }
  | {
      type: "screenshotCheckpoint";
      state: string;
    };

export type CaptureTarget = {
  captureId: string;
  product: "fifa" | "chess";
  viewport: "desktop" | "mobile";
  pageArea: string;
  state: string;
  url: string;
  relatedPa1Figure?: string;
  relatedPa1UseCase?: string;
  requiresAuth?: boolean;
  captureBeforePopupDismiss?: boolean;
  actions?: CaptureAction[];
};

export type CaptureStatus =
  | "SUCCESS"
  | "PARTIAL"
  | "BLOCKED"
  | "MISSING_CURRENT_STATE"
  | "FAILED";

export type AuthenticationState =
  | "PUBLIC"
  | "GUEST"
  | "AUTHENTICATED_EXISTING_SESSION"
  | "LOGIN_REQUIRED"
  | "UNKNOWN";

export type ManifestRow = {
  capture_id: string;
  product: string;
  viewport: string;
  page_area: string;
  state: string;
  source_url: string;
  final_url: string;
  page_title: string;
  filename: string;
  absolute_path: string;
  captured_at_local: string;
  width_px: string;
  height_px: string;
  file_size_bytes: string;
  document_scroll_width: string;
  document_scroll_height: string;
  auto_scroll_iterations: string;
  reached_bottom: string;
  popup_action: string;
  authentication_state: AuthenticationState;
  status: CaptureStatus;
  attempt_count: string;
  failure_reason: string;
  related_pa1_figure: string;
  related_pa1_use_case: string;
  notes_factual_only: string;
};

export type AttemptLog = {
  timestamp: string;
  captureId: string;
  project: string;
  attempt: number;
  viewport: string;
  sourceUrl: string;
  finalUrl: string;
  navigationResult: string;
  popupAction: string;
  actionResult: string;
  autoScrollResult: string;
  screenshotResult: string;
  outputPath: string;
  errorClass: string;
  errorMessage: string;
  status: CaptureStatus;
};
